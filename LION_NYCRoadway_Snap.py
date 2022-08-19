#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing the necessary libraries
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import requests
import fiona
import io
from fiona.io import ZipMemoryFile
import zipfile
from zipfile import ZipFile
from shapely.ops import snap


# In[4]:


# specifying the zip file name
file_name1 = "RoadwayInventorySystem_2263.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name1, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
    
file_name2 = "LION_22.zip"
  
with ZipFile(file_name2, 'r') as zip:
    zip.printdir()
  
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')


# In[5]:


#reading the NYC Roadways file
roadway = gpd.read_file('RoadwayInventorySystem_2263')
#creating GeoDataFrame in 2236 crs
roadway_gdf = gpd.GeoDataFrame(roadway, geometry = 'geometry',crs = 'epsg:2236')
roadway.head()


# In[6]:


#reading the LION file
lion = gpd.read_file('LION_22')
#creating GeoDataFrame in 2236 crs
lion_gdf = gpd.GeoDataFrame(lion, geometry = 'geometry',crs = 'epsg:2236')
lion_gdf.head()


# In[7]:


#plotting the NYC Roadways map
roadway_gdf.plot()


# In[8]:


#plotting the LION map
lion_gdf.plot()


# In[10]:


lion_to_roadway_union = gpd.overlay(lion_gdf, roadway_gdf, how = 'union')
lion_to_roadway_union.head()


# In[11]:


ax = lion_to_roadway_union.plot(alpha=0.7, figsize=(20, 10))

lion.plot(ax = ax, facecolor = 'none', edgecolor = 'g')
roadway.plot(ax = ax, facecolor = 'none', edgecolor = 'w')

plt.title("LION and NYC Roadways")

