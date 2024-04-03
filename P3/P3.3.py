import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

# Define center of area of interest and projection type
central_lon, central_lat = 18.5, -34.2
fig, ax = plt.subplots(1,3,figsize=(15,10),subplot_kw={'projection':ccrs.Orthographic(central_lon, central_lat)})

# Call different resolution level GSHHG data
cl_low = cfeature.GSHHSFeature(scale='coarse')
cl_int = cfeature.GSHHSFeature(scale='intermediate')
cl_high = cfeature.GSHHSFeature(scale='full')

# Define parameters for each subplot
res = [cl_low, cl_int, cl_high]
lab = ['Coarse','Intermediate','High']
gl = ['gl0', 'gl1', 'gl2']
extent = [18.2, 19, -34.5, -33.8]

# Iterate defined features over each plot and clean up labeling
for i in range(0,3):
    ax[i].set_extent(extent)
    ax[i].add_feature(res[i])
    ax[i].set_title(lab[i])
    gl[i] = ax[i].gridlines(draw_labels=True)
    gl[i].right_labels = False
    gl[i].top_labels = False

# Add title to figure and plot
fig.suptitle('False Bay', fontsize = 24, y=0.75)
plt.show()



#%%
coord=[30.3,33.0,-116.5,-119.72]
cropped_ds = ds.sel(lat=slice(coord[0], coord[1]), lon=slice(coord[2],coord[3]))