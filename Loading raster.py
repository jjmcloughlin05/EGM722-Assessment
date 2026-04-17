import matplotlib
import pandas as pd
import glob
from pathlib import Path
import os
from shapely.geometry import Point, LineString, Polygon
import rasterio as rio
import geopandas as gpd
import matplotlib.pyplot as plt
from rasterio.plot import show

parent = Path("C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/")

data = {}

for subfolder in parent.iterdir():
    if subfolder.is_dir():
        files = [f.name for f in subfolder.iterdir() if f.is_file()]
        data[subfolder.name] = files

print(data)


'''
parent = Path("C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/")

rows = []

for subfolder in parent.iterdir():
    if subfolder.is_dir():
        for f in subfolder.iterdir():
            if f.is_file():
                rows.append({
                    "folder": subfolder.name,
                    "file": f.name,
                    "path": str(f)
                })

print(rows)
# Example: convert to DataFrame
import pandas as pd
df = pd.DataFrame(rows)
'''

'''
parent = Path("C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/")

data = {}

for subfolder in parent.iterdir():
    if subfolder.is_dir():
        files = [f.name for f in subfolder.iterdir() if f.is_file()]
        data[subfolder.name] = files

print(data)
'''




#subfolders = []
#\parent ='C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/'
#subfolders = os.listdir(parent)
#for f in subfolders:
#    print(f)
#   # print(subfolders[f])
#    band_files = glob.glob(os.path.join(parent,f, "*_SR_B*.TIF"))
#    print(band_files)

#print(type(subfolders))


'''
folder = 'C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/LC08_L2SP_043034_20130815_20200912_02_T1/'
band_files = glob.glob(os.path.join(folder, "*_SR_B*.TIF"))
band_files.sort()

print("Found files:")
for f in band_files:
    print(f)

'''
'''
dataset = rio.open('C:/RS_GIS/EGM713/Assignment II/Data/Summer/Raw/LC08_L2SP_043034_20130815_20200912_02_T1/LC08_L2SP_043034_20130815_20200912_02_T1_SR_B6.TIF')
boundary = gpd.read_file('C:/RS_GIS/EGM713/Assignment II/AOI/aoi.shp')

# Match CRS
boundary = boundary.to_crs(dataset.crs)

fig, ax = plt.subplots(figsize=(10, 10))
show(dataset, ax=ax, cmap='pink')
boundary.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=2)
plt.show()
'''
'''
def load_data():
    global time_series

    time_series = {}

    for folder in folders:
        band_files = glob.glob(os.path.join(folder, "*_SR_B*.TIF"))
        band_files.sort()

        band_dict = {}

        for path in band_files:
            filename = os.path.basename(path)
            band_name = filename.split("_")[-1].replace(".TIF", "")
            band_dict[band_name] = path

        time_series[folder] = band_dict

    for folder, bands in time_series.items():
        print(f"\nFolder: {folder}")
        for band, path in bands.items():
            print(f"  {band} → {path}")
'''


'''
import glob
import os
from datetime import datetime
import rasterio


# Helper Functions
def add_parent_folder():
    parent = filedialog.askdirectory(title="Select parent folder")

    if not parent:
        return

    subfolders = [os.path.join(parent, f) for f in os.listdir(parent)
                  if os.path.isdir(os.path.join(parent, f))]

def dataset_info():
    global time_series

    time_series = {}

    # clear table first
    for row in table.get_children():
        table.delete(row)

    for folder in folders:
        band_files = glob.glob(os.path.join(folder, "*_SR_B*.TIF"))
        band_files.sort()

        band_dict = {}

        for path in band_files:
            filename = os.path.basename(path)
            satellite, pathrow, date, band = parse_landsat_name(filename)
            role = get_band_role(satellite, band)
            scene_id = f"{satellite}_{pathrow}_{date}"
            #band_name = filename.split("_")[-1].replace(".TIF", "")
            band_dict[band] = path

            # add row to table
            table.insert("", tk.END, values=(satellite, scene_id, date, band, role, filename))
        time_series[folder] = band_dict

def parse_landsat_name(filename):
    parts = filename.split("_")
    satellite = parts[0]  # LC08
    pathrow = parts[2]
    date_raw = parts[3]  # 20130815
    band = parts[-1].replace(".TIF", "")  # B6

    # convert YYYYMMDD → DD/MM/YYYY
    date = datetime.strptime(date_raw, "%Y%m%d").strftime("%d/%m/%Y")

    return satellite, pathrow, date, band,

def get_band_role(satellite, band):
    if satellite == "LC08":
        mapping = {
            "B2": "BLUE",
            "B3": "GREEN",
            "B4": "RED",
            "B5": "NIR",
            "B6": "SWIR1",
            "B7": "SWIR2"
        }
    elif satellite in ["LT05", "LE07"]:
        mapping = {
            "B1": "BLUE",
            "B2": "GREEN",
            "B3": "RED",
            "B4": "NIR",
            "B5": "SWIR1",
            "B7": "SWIR2"
        }
    else:
        mapping = {}

    return mapping.get(band, "UNKNOWN")

folders = []
print("Final folders:", folders)
'''