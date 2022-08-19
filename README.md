## Introduction
The NYC DOT has requested the creation of a script to snap LION to NYC Roadways since the geospatial data are in two different coordinate systems, making data maintenance harder.

## Installing GeoPandas
To install the latest development version of GeoPandas, you can clone the GitHub repository and use the setup script:
```sh
git clone https://github.com/geopandas/geopandas.git
cd geopandas
pip install .
```

## Dependencies
```sh
numpy
pandas
shapely
fiona
six
pyproj
```
Installing the conda package from the conda-forge channel should also install all dependencies automatically:
```sh
conda install -c conda-forge geopandas
```
