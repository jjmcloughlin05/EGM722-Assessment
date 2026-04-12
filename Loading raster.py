'''

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

import tkinter as tk
from tkinter import filedialog
import glob
import os

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Open folder selection dialog
folder = filedialog.askdirectory(title="Select folder with band data")

print("Selected folder:", folder)

# Find all band files
band_files = glob.glob(os.path.join(folder, "*_SR_B*.TIF"))
band_files.sort()

print("Found files:")
for f in band_files:
    print(f)
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


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import glob
import os
from datetime import datetime
import rasterio


# Helper Functions
def add_folder():
    folder = filedialog.askdirectory(title="Select dataset folder")
    if folder and folder not in folders:
        folders.append(folder)
        update_list()


def add_parent_folder():
    parent = filedialog.askdirectory(title="Select parent folder")

    if not parent:
        return

    subfolders = [os.path.join(parent, f) for f in os.listdir(parent)
                  if os.path.isdir(os.path.join(parent, f))]

    for folder in subfolders:
        if folder not in folders:
            folders.append(folder)

    update_list()

def remove_selected():
    selected = listbox.curselection()
    for i in reversed(selected):
        folders.pop(i)
    update_list()

def update_list():
    listbox.delete(0, tk.END)
    for f in folders:
        listbox.insert(tk.END, f)

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

# Main window
root = tk.Tk()
root.title("Dataset Manager")
root.geometry("1000x700")

# Layout frame
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Listbox (shows selected folders)
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox.pack(fill=tk.BOTH, expand=True)

# Treeview table (dataset info)
table = ttk.Treeview(root, columns=("satellite", "scene_id", "date", "band", "role", "filename"), show="headings")

table.heading("satellite", text="Satellite")
table.heading("scene_id", text="Scene ID")
table.heading("date", text="Date")
table.heading("band", text="Band")
table.heading("role", text="Role")
table.heading("filename", text="Filename")

table.column("satellite", width=80)
table.column("scene_id", width=80)
table.column("date", width=80)
table.column("band", width=100)
table.column("role", width=60)
table.column("filename", width=100)

table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Folder", command=add_folder).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Add Parent Folder", command=add_parent_folder).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Remove Selected", command=remove_selected).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Data Set Info", command=dataset_info).pack(side=tk.LEFT, padx=5)
#tk.Button(root, text="Load Data", command=load_data).pack(pady=5)

root.mainloop()

print("Final folders:", folders)