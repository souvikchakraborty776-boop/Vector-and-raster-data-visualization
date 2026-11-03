"""
3. Vector data Loading and Visualization
"""

pip install geopandas

from google.colab import drive
drive.mount('/content/drive')

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import geopandas as gpd
from pathlib import Path

# Set max rows displayed for readability
pd.set_option("display.max_rows", 6)
# Plot settings
plt.style.use(
    "https://github.com/aeturrell/coding-for-economists/raw/main/plot_style.txt"
)
# For this chapter, some bespoke settings:
plt.style.use(
    {
        "axes.autolimit_mode": "data",
        "patch.linewidth": 0.2,
        "figure.figsize": (10, 8),
        "figure.dpi": 125,
    }
)

import matplotlib_inline.backend_inline

matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# To run this example, you will need to download the files at this url:
# https://github.com/aeturrell/coding-for-economists/tree/main/data/geo/world
# and save them in the path 'data/geo/world' (path relative to where you're running the code)
df = gpd.read_file(Path("/content/drive/MyDrive/ADITI_SHP/WARD_AUTOCOMPLETE.shp"))
df.head(10)
#df.tail(5)

df.plot(color="red");

"""
4. Raster data Loading and Visualization
"""

pip install rasterio

import seaborn as sn
import rasterio
from rasterio import plot

mss= rasterio.open('/content/drive/MyDrive/Sentinal/sentinel 2a.img')
mss.count

georef=mss.meta
print(georef)

fig= plt.figure()
plot.show(mss)

green = mss.read(1)
red= mss.read(3)
nir=mss.read(4)
print(green)
print(red)
print(nir)