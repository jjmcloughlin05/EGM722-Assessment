# EGM722-Assessment

## 1. Project Setup and Installation

### 1.1 System Requirements & Dependencies
A package and environment management system like **Conda (Miniconda/Anaconda)** is recommended. 

### 1.2 **Recommended IDEs:** 
* PyCharm 
* JupyterLab / Notebook

### 1.3 **Dependencies:**
* Python 3.11+
* pip
* numpy
* pandas
* scipy
* earthaccess
* geopandas
* rasterio
* rasterstats
* rioxarray
* xarray
* xarray-spatial
* shapely
* matplotlib
* matplotlib-scalebar
* notebook


---

### 1.4 Installation
1.4.1. **Clone the Repository**  
   Clone the repository to access all necessary scripts and test data.
   ```bash
   git clone https://github.com/jjmcloughlin05/EGM722-Assessment
   ```

1.4.2. **Environment Setup**  
   The included `environment.yml` file contains the full list of dependencies. Create the environment using:
   ```bash
   conda env create -f environment.yml
   ```

1.4.3. **NASA EarthAccess Authorization**  
   To download data, you must have a [NASA Earthdata account](https://nasa.gov). Once registered, create a `.netrc` file in your home directory with your credentials in the following format:
   ```text
   machine urs.earthdata.nasa.gov login <username> password <password>
   ```

---

### 1.5 Directory Structure
* If the full repository was cloned then no further actions need to be taken.
* If the repository was only partially cloned ensure the following directories are created (**Note:** Subdirectory names must match the structure exactly):

```text
Data/
├── Landsat_Rasters/       # Store Landsat imagery here
├── Vector_Layers/         # Store ROI shapefiles here
```

---

### 1.6 Sample Data 
* If the full repository was cloned then no further actions need to be taken.
* If the repository was only partially cloned ensure the following files are present:

1.6.1 **Landsat Images**
The script processes Landsat Level-2 Surface Reflectance data. The following sample data is highly recommended, and available from USGS EarthExplorer:
* LC09_L2SP_037035_20250627_20250628_02_T1
* LC09_L2SP_038035_20250704_20250705_02_T1

* **Storage:** Place in `Data/Landsat_Rasters`. 
* **Format:** Files must retain NASA naming conventions. To save space, you may delete all files except those ending in `SR_B*.TIF`.

1.6.2 **Region of Interest Shapefile**
A shapefile is used to define the study area (Region of Interest) to optimize memory and filter searches.
* **Data:** Grand Canyon National Park boundary (ArcGIS Online).
* **Storage:** `Data/Vector_Layers/national_park_boundary.shp`
* **Format:** Must be in .shp format.

---

## 2. Executing scripts
To successfully execute either script the path of the `Data` directory must first be mapped. This is implemented within the Configuration section at the start of each script, immediately after the module imports