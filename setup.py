#! /usr/bin/env python
from setuptools import setup, find_packages
setup(
    name = 'pyspatialite',
    version = '0.2',
    packages=['pyspatialite'],
    description = 'DB-API 2.0 interface for SQLite 3.x with Spatialite',
    author = 'Lokkju Brennr',
    author_email = 'lokkju@lokkju.com',
    license = 'zlib/libpng license',
    platforms = 'ALL',
    url = 'https://github.com/lokkju/pyspatialite/',
    # no download_url, since pypi hosts it!
    #download_url = 'http://code.google.com/p/pyspatialite/downloads/list',
    package_data={
        'pyspatialite': ['*.dll', '*.pyd'],
    }
)