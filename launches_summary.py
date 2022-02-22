#!/usr/bin/env python

#from spacex_py import launches
from spacex_api import launches
from collections import Counter
import pandas as pd
import openpyxl as xl
import operator

# Getting data from SpaceX API
launches_summary, header = launches.get_launches()

launch_year = []
launch_site = []

for d_launch in launches_summary:
    launch_year.append(d_launch.get('launch_year'))
    launch_site.append(d_launch.get('launch_site').get('site_name'))

# Counting how many launches happened per year
launch_per_year = {i: launch_year.count(i) for i in launch_year}
max_launch_year = max(launch_per_year.items(), key=operator.itemgetter(1))[0]
max_launch_year_launches = max(launch_per_year.items(),
                               key=operator.itemgetter(1))[1]

# Counting how many launches happened per site
# (using a method with better performance than above the one)
launch_per_site = Counter(launch_site)
max_launch_site = launch_per_site.most_common(1)

# Counting how many launches happenned in a defined range of years
year_low, year_top = 2019, 2021
launches_range = {key: val for key, val in filter(lambda sub:
                                                  int(sub[0]) >= year_low and
                                                  int(sub[0]) <= year_top,
                                                  launch_per_year.items())}
n_launches_range = sum(launches_range.values())

# Exporting results to a xlsx file
file_name = 'launches_summary.xlsx'
book = xl.Workbook()

summary_sheet = book.active
summary_sheet.title = 'Summary'
summary_sheet['A1'] = 'Year with most launches is'
summary_sheet['B1'] = int(max_launch_year)
summary_sheet['C1'] = '(' + str(max_launch_year_launches) + " launches)"

summary_sheet['A2'] = 'Site with most launches is'
summary_sheet['B2'] = max_launch_site[0][0]
summary_sheet['C2'] = '(' + str(max_launch_site[0][1]) + " launches)"

summary_sheet['A3'] = ('Number of launches between ' + str(year_low)
                       + ' and ' + str(year_top) + ' is')
summary_sheet['B3'] = n_launches_range

# Formating a bit the table
summary_sheet['C1'].alignment = xl.styles.Alignment(horizontal='right')
summary_sheet['B2'].alignment = xl.styles.Alignment(horizontal='right')
summary_sheet['C2'].alignment = xl.styles.Alignment(horizontal='right')
summary_sheet.column_dimensions['A'].width = 50
summary_sheet.column_dimensions['B'].width = 15
summary_sheet.column_dimensions['C'].width = 15

book.save(file_name)

# Exporting also the number of launchers per year and per site
writer = pd.ExcelWriter(file_name, engine='openpyxl')
writer.book = book

data_export = pd.DataFrame(list(launch_per_year.items()),
                           columns=['Year', '# Launches'])
data_export.to_excel(writer, sheet_name='Lauchers_per_year')
summary_sheet = book['Lauchers_per_year']
summary_sheet.column_dimensions['C'].width = 12

data_export = pd.DataFrame(list(launch_per_site.items()),
                           columns=['Site', '# Launches'])
data_export.to_excel(writer, sheet_name='Lauchers_per_site')
summary_sheet = book['Lauchers_per_site']
summary_sheet.column_dimensions['B'].width = 15
summary_sheet.column_dimensions['C'].width = 12

writer.save()
writer.close()
