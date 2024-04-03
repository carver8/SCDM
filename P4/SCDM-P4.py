#%% Assignment P4 - Cameron Carver
## Import relevant libraries
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

ds = xr.open_dataset('ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')    # import chlor dataset
bth = xr.open_dataset('GMRTv4_2_20240401topo.grd')      # import bathymetry dataset
coord=[33.0,30.3,-119.72,-116.5]                        # define area of interest
cropped_ds = ds.sel(lat=slice(coord[0], coord[1]), lon=slice(coord[2],coord[3]))        # slice out chlorophyll data for area of interest
chlor = cropped_ds['chlor_a']                           # define chlorophyll data

#%% Part 1 - Bathymetry
fig = plt.figure(figsize=(12, 8));                      # create figure
ax1 = plt.axes(projection=ccrs.PlateCarree())           # plot projection
bthy = ax1.contourf(bth['lon'],bth['lat'],bth['altitude'],transform=ccrs.PlateCarree(),cmap="Blues_r")  # plot bathymtry data with appropraite color
ax1.coastlines()                                        # add coastlines
gl1 = ax1.gridlines(draw_labels=True); gl1.right_labels = False; gl1.top_labels = False # add gridlines and remove excess labels
fig.colorbar(bthy, ax=ax1, label="Depth (m)", aspect=25);   # specify colorbar parameters
ax1.set_title("Bathymytry of Baja California West Coast")   # set title

#%% Part 2 - Mean Chlorophyll
chlor_mean = chlor.mean(dim='time')                     # set dimension to time
fig = plt.figure(figsize=(12, 8))                       # define figure
ax2 = plt.axes(projection=ccrs.PlateCarree()); ax2.coastlines();        # plot projection and coastlines
chlor_mean.plot.contourf(levels=np.arange(0,7,0.01),cmap='turbo',
                         cbar_kwargs={"label": "Chlorophyll Concentration mg $m^{-3}$"}) # plot contour based on chlorophyll data 
gl2 = ax2.gridlines(draw_labels=True); gl2.right_labels = False; gl2.top_labels = False # add gridlines and remove excess labels 
ax2.set_title("Mean Annual Chlorophyll of Baja California West Coast")  # set title

#%% Part 3 - Monthly Averages
monthly_mean = chlor.groupby('time.month').mean()               # group chlorophyll by month and take the monthly mean
monthly_mean = monthly_mean.reindex(month=np.arange(1,13,1))    # reindex to match months
facet = monthly_mean.plot(levels=np.arange(0,10,0.01), col='month', col_wrap=4,
                          cmap='turbo',cbar_kwargs={"label": "Chlorophyll Concentration mg $m^{-3}$"}) # plot monthly means
facet.fig.suptitle("Monthly Average of Chlorophyll Concentration on West Coast of Baja California",y=1) # Set title

#%% Part 4 - Time Series
plt.figure(figsize=(12,8))                                  # define figure
chlor = chlor.sortby('time')                                # sort chlorophyll data by time
seasonal = chlor.resample(time='QS-Dec').mean()             # resample chlorophyll data into seasonal bins starting at December
seasarea = seasonal.groupby('time').mean(["lat","lon"])     # seasonal mean of area
seaspt = seasonal.sel(lat=31.9,lon=-116.8,method='nearest') # seasonal mean of point

fig = plt.figure(figsize=(12, 8)); ax4 = plt.axes() # define figure and axes
seasarea.plot(ax=ax4, marker='^')   # plot seasonal average of area of interest
seaspt.plot(ax=ax4, marker='o')     # plot seasonal average at defined point

ax4.set_xlabel("Time (Year-Month)"); ax4.set_ylabel("Chlorophyll Concentration mg $m^{-3}$")# define x and y labels
ax4.set_title("Mean Seasonal Chlorophyll Concentration along Baja California")              # set title
plt.legend(['Overall Defined Area','Nearest Single Point: 31.9ºN 116.8ºW']); plt.grid()     # define legend and add gridlines

