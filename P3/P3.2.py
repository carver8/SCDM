import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='educational')

fig = plt.figure(figsize=[10, 10])
ax = plt.axes(projection=ccrs.Mollweide())

extent = [-60, 27, -42, -19]
ax.set_extent(extent)

ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.BORDERS, lw=0.2)
ax.add_feature(cfeature.COASTLINE, lw=0.7)
gl = ax.gridlines(draw_labels=True,x_inline=False, color='k', linewidth=0.2)
gl.right_labels = False
gl.top_labels = False
ax.set_title('Southern Atlantic Ocean')

place = ['Cape Town','Walvis Bay','Rio de Janeiro','Montevideo']
address = []
for p in place:
    loc = geolocator.geocode(p,language="en")
    address.append(loc)

for p in range(len(place)):
    ax.text(address[p].longitude+1,address[p].latitude,place[p],transform=ccrs.Geodetic())
    plt.scatter(address[p].longitude,address[p].latitude, transform=ccrs.Geodetic(), color='#000080')
