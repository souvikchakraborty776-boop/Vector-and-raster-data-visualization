# Vector-and-raster-data-visualization
A Python script demonstrating how to load, explore, and visualize geospatial vector data (shapefiles) using GeoPandas and raster data (Sentinel-2 imagery) using Rasterio in Google Colab.
# Geospatial Data Visualization in Python

This repository contains a Python script for loading, exploring, and visualizing both vector and raster geospatial data using Google Colab. 

## Overview
The script demonstrates foundational geospatial workflows:
* **Vector Data:** Loads and visualizes polygon shapefiles using `geopandas` and `matplotlib`.
* **Raster Data:** Loads multispectral imagery (Sentinel-2), extracts metadata, and reads specific image bands (Green, Red, Near-Infrared) using `rasterio`.

## Prerequisites
The script is designed to run in **Google Colab** and requires connecting to Google Drive. The following Python libraries are used:
* `geopandas`
* `rasterio`
* `matplotlib`
* `pandas`
* `seaborn`
* `numpy`

## Usage Instructions

1. **Environment:** Open the script in Google Colab.
2. **Mount Drive:** The script automatically mounts your Google Drive to access local datasets. Allow the necessary permissions when prompted.
3. **Install Dependencies:** The script includes inline `pip install` commands for `geopandas` and `rasterio`.
4. **Update File Paths:** You will need to update the file paths in the script to match the locations of your own geospatial files in your Google Drive:
   * **Vector:** Update the `.shp` file path (currently set to `/content/drive/MyDrive/ADITI_SHP/WARD_AUTOCOMPLETE.shp`).
   * **Raster:** Update the `.img` or `.tif` file path (currently set to `/content/drive/MyDrive/Sentinal/sentinel 2a.img`).

## Outputs
* A red-filled boundary plot of the vector shapefile.
* A printed output of the raster's spatial metadata (coordinate reference system, transform, bounds).
* A visual plot of the raster image and array outputs for individual spectral bands.
