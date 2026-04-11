import rasterio
import matplotlib
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt
from rasterio.plot import show

dataset = rasterio.open('C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/LC08_L2SP_043034_20130815_20200912_02_T1/LC08_L2SP_043034_20130815_20200912_02_T1_SR_B6.TIF')
boundary = gpd.read_file('C:/RS_GIS/EGM713/Assignment II/AOI/aoi.shp')

# Match CRS
boundary = boundary.to_crs(dataset.crs)

fig, ax = plt.subplots(figsize=(10, 10))
show(dataset, ax=ax, cmap='pink')
boundary.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=2)
plt.show()

