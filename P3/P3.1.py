import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[10, 10])
prj = ccrs.Orthographic(central_longitude=0,central_latitude=-90)
ax1 = plt.subplot(1, 1, 1, projection=prj)

y_max, y_min = prj.transform_point(0, -60, ccrs.PlateCarree())
x_max, x_min = prj.transform_point(-90, -60, ccrs.PlateCarree())

extent = [y_min, x_max, y_min, x_max]
ax1.set_extent(extent, crs=prj) # data/projection coordinates

ax1.add_feature(cfeature.OCEAN)
ax1.add_feature(cfeature.LAND)
ax1.coastlines(lw=1)

ax1.gridlines(draw_labels=True, x_inline=False, color ='k', y_inline=True, linewidth=0.5)
ax1.set_title('Antarctica & Southern Ocean below 60ºS')
plt.show()
#%%
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[8, 8])
ax1 = fig.add_subplot( projection=ccrs.SouthPolarStereo())
ax1.set_extent([-180, 180, -90, -59], ccrs.PlateCarree())

ax1.add_feature(cfeature.LAND)
ax1.add_feature(cfeature.OCEAN)
ax1.coastlines(lw=1)

ax1.gridlines(draw_labels=True, color ='k',linewidth=0.5, rotate_labels=180, xpadding=10)
ax1.set_title('Antarctica & Southern Ocean below 60ºS')
plt.show()