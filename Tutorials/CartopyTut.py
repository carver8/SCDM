import cartopy.crs as ccrs
import matplotlib.pyplot as plt

central_lon, central_lat = 18, -34.5
extent = [17, 22, -35, -32]
fig,ax = plt.subplots(1,2,figsize=(10,6),subplot_kw={'projection':ccrs.Orthographic(central_lon, central_lat)})

ax[0].set_extent(extent)
gl0 = ax[0].gridlines(draw_labels=True)
ax[0].coastlines(resolution='50m')

ax[1].set_extent(extent)
gl1 = ax[1].gridlines(draw_labels=True)
ax[1].coastlines(resolution='10m')

gl0.right_labels = False
gl0.top_labels = False
gl1.left_labels = False
gl1.top_labels = False

import cartopy.feature as cfeature
import numpy as np

extent = [0, 40, 30, -40]           #Lat/Long Bounds
central_lon = np.mean(extent[:2])   #
central_lat = np.mean(extent[2:])

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cfeature.OCEAN)              #Ocean imported as blue
ax.add_feature(cfeature.LAND, edgecolor='black') #Define land edge color to black
ax.add_feature(cfeature.LAKES, edgecolor='black') #Define lake adge as black
ax.add_feature(cfeature.RIVERS)      #Rivers imported as blue
ax.gridlines(draw_labels=True)


# create some test data
new_york = dict(lon=-74.0060, lat=40.7128)
honolulu = dict(lon=-157.8583, lat=21.3069)
lons = [new_york['lon'], honolulu['lon']]
lats = [new_york['lat'], honolulu['lat']]

ax = plt.axes(projection=ccrs.PlateCarree())
ax.plot(lons, lats, label='Equirectangular straight line')
ax.plot(lons, lats, label='Great Circle', transform=ccrs.Geodetic())
ax.coastlines()
ax.legend()
ax.set_global()

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent='educational') # nominatim is a free service and requires an identificative agent
CT = geolocator.geocode('Cape Town') 
SANAE = geolocator.geocode('SANAE IV')
print(type(CT))
print(CT)
print(SANAE)
print('The distance is ',geodesic(CT.point,SANAE.point).km,' km')