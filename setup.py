from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='spacex_api',
    version='1.0.0',
    description='Simple package for accessing SpaceX API.',
    long_description=readme,
    author='Thiago Bezerra',
    author_email='thiagojcb@gmail.com',
    url='https://github.com/thiagojcb/spacex_api',
    license=license,
    packages=find_packages(exclude=('tests')),
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests"
    ]

)

