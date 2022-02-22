Module to access SpaceX	API
========================

This simple project accesses the [SpaceX API](https://docs.spacexdata.com/#bc65ba60-decf-4289-bb04-4ca9df01b9c1) to get their rocket launches information.

It also contains a data selection script, that compiles some information of interest.

## Dependencies	
- Module:	`requests`, `pytest`
- Simple data selection: `pandas`, `openpyxl`

## Install

Once you cloned	this repository, on its	main directory do:

```BASH
$ pip install .
```

## Usage

```PYTHON
from spacex_api import launches

# Returns a tuple
got_launches, header = launches.get_launches()

# Prints list of launches
print(got_launches)
```

## Simple data selection
Run the following:
```BASH
$ python launches_summary.py
```
The script above will:
- Indentify the year that has most launches
- Indentify the site where most launches happened
- Retrieve the number of launches in a specificy range of years (2019, 2021)
- The above information is exported to a `.xlsx` file (`launches_summary.xlsx`)

## Module tests
The test below will check if the API is being accessed successfully.
```BASH
$ pytest -v tests/
```

## References
- This module is a simplification of [SpaceX-PY](https://github.com/hikaylum/spacex-py)
- This module's structure is based on [Sample Module Repository](https://github.com/navdeep-G/samplemod)
