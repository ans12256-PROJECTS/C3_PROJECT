# August 3, 2021
# Code to display geo locations of Google Places
# run from directory above src
#  since paths are relative and are hard coded
#
# python src/Map_plot.py

# check if geopandas is available:
import time  # for execution time reference
start_total = time.time()

import sys

# https://stackoverflow.com/questions/20957811/how-to-check-if-a-module-is-available-for-import
if 'geopandas' in sys.modules:
    print ('geopandas is available')
else:
    print ('geopandas is not available') # for whatever reason prints this when in fact is available

# redundant, just for the record

try:
    import geopandas as gpd
except ImportError:
    print('Geopandas is not available. Please "conda install geopandas",\n \
    or switch environment where geopandas is installed "conda activate geopandas_env_name"')
    sys.exit(0)
# the rest of your code

import numpy as np
import pandas as pd

import time  # for execution time reference

# users.json 764.2 Mb
# places.json 1.07 Gb
# reviews.json 4.57 Gb
print("Importing df = pd.read_json('data/places.json')")
df = pd.read_json('data/places.json')  # Wall time: 1min 14s, Memory: 9.5 GB
print('DONE')
# df.shape # (3,114,353, 8)
# df.columns ['name', 'price', 'address', 'hours', 'phone', 'closed', 'gPlusPlaceId', 'gps']
# df.gps[0] [33.703804, -117.003209]
# in the Southern hemisphere (negative latitudes)
# df.gps[0][0] # 33.703804 latitude North-South
# Positive longitudes are east of the prime meridian, and negative ones are west
# df.gps[0][1] # -117.003209 longitude East-West
# df.address[0] # ['2615 Angler Ave', 'Hemet, CA 92545'] Checks out in google maps

# df.gps.dropna().shape # df.gps.shape (3114353,) #df.gps.dropna().shape (3087402,), 26951 no gps data
print('Splitting list of GPS coordinates')
gps = pd.DataFrame(df.gps.dropna().to_list(), columns = ['NS_latitudes','EW_longitudes']) #.str.split(',', expand=True)
print('DONE, preparing image img/Places_TOTAL.png. Image will NOT be shown')
# prepare geopandas data
# https://github.com/chrisshaffer/fraud-detection-case-study/blob/main/src/Map_Plots.ipynb
# GPS plots
import matplotlib.pyplot as plt
# import geopandas as gpd  # import is moved up for safe exit if not available
countries = gpd.read_file(
               gpd.datasets.get_path("naturalearth_lowres"))
countries.head()

# make fonts larger
font_size = 20
plt.rc('font', size=font_size) #controls default text size
plt.rc('axes', titlesize=font_size) #fontsize of the title
plt.rc('axes', labelsize=font_size) #fontsize of the x and y labels
plt.rc('xtick', labelsize=font_size) #fontsize of the x tick labels
plt.rc('ytick', labelsize=font_size) #fontsize of the y tick labels
plt.rc('legend', fontsize=font_size) #fontsize of the legend

# There are not only NaNs, but lost decimal comas in gps
# coordinates, resulting in huge numbers
# to clean abs(EW_gps) <= 180, abs(NS_gps) <=90
# in addition only when both gps coordinates are valid,
#  proceed to plot. Here is a check of boolean

# Combined filter can only be true if both coordinates are correct
# ser1 = pd.Series([True,True,False,False])
# ser2 = pd.Series([True,False,True,False])
# ser1 & ser2 # results in True only for the first row

EW_filter=abs(gps.EW_longitudes) <= 180
# > 180 False    3012033, True       75369
# <= True     3012033, False      75369 (2.44%) 75369/3087402*100
gps.EW_longitudes[EW_filter].hist()
EW_filter.value_counts()  # ~ -3087403
# EW_filter

NS_filter=abs(gps.NS_latitudes) <= 90
# <= True     3011647, False      75755 (2.45%) 75755/3087402*100
gps.NS_latitudes[NS_filter].hist()
NS_filter.value_counts()  # ~ -3087403
# NS_filter

gps_value_filter = EW_filter & NS_filter # only True True pairs result in True
# True     3011584, False      75818 (2.45%) 75818/3087402*100
gps_value_filter.value_counts()

# Now the fun part
countries.plot(color="lightgrey", figsize=(20,15)) # color="lightgrey"
# s=1 - smallest marker
plt.scatter(gps.EW_longitudes[gps_value_filter],
            gps.NS_latitudes[gps_value_filter], s=1,
            color='b', label='Google Places')

plt.title('OVERALL Google places locations')
box = {'facecolor': 'gold',
       'edgecolor': 'black',
       'boxstyle': 'round'
      }
plt.text(-150, -50, '3M places\nworldwide', bbox=box)
plt.legend()
plt.grid()
# bbox_inches='tight' save without extra padding
plt.savefig('img/Places_TOTAL.png',
facecolor='w', edgecolor='w',
transparent=False, bbox_inches='tight')

print(f'Total run time: {round((time.time() - start_total)/60, 2)} minutes')
