import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Load the CSV file in python, using the appropriate column for the time index. 
# Check that the missing values are properly recognized.
# The ship reached the southernmost location on July 4th. 
# Use the time indexing to select the data from departure to that date included. 
# All plots will be done using this selected set of data.
data = pd.read_csv('SAA2_WC_2017_metocean_10min_avg.csv', index_col=1)  #import data from file with date time as indexing column
outbound=data.loc[:'2017/07/05']            #select all indexed values up through July 4th


# Plot the time series of temperature with the appropriate labels.
plt.figure(1) 
plt.style.use('grayscale')                  #Set plot style to grayscale
fig, ax = plt.subplots()
ax.plot(outbound.index, outbound['TSG_TEMP'])    #Plot air temperaure over time
ax.set_xlabel("Date & Time")                            #Label x axis
ax.set_ylabel("Temperature (ºC)")                       #Label y axis
ax.set_title("TSG Temperature")                         #Set title
hours = mdates.DayLocator(interval = 72)                #Identify periodic time interval for xticks
ax.xaxis.set_major_locator(hours)                   #Set xtick to identified interval
plt.xticks(rotation=70)                             #Rotate x labels to be readable
plt.show()

# Save the figure using the 'grayscale' style
fig.tight_layout()                          #Ensure all of plot fits in window
fig.savefig("SCDM_P2_timescale.png")             #Save fig

# Plot a histogram of salinity using bins of 0.5 psu between 30 and 35
plt.figure(2)
plt.style.use('default')                #Set plot syle to default
fig, ax = plt.subplots()
ax.hist(outbound['TSG_SALINITY'],edgecolor='black', bins=np.arange(30,35.5,0.5)) #Plot salinity values between 30 and 35 in histogram with bin size of 0.5
ax.set_xlabel("Salinity (ppt)")             #Set x axis label
fig.tight_layout()                          #Ensure all of plot fits in window
fig.savefig("SCDM_P2_hist.png")             #Save fig

# Create a scatter plot of wind speed and air temperature, encoding the latitude information in color. 
# Wind speed is in meters per second and air temperature in degrees C.
plt.figure(3)
fig, ax = plt.subplots()
ddmm=outbound[['LATITUDE']]
def ddmm2dd(ddmm):                      
    thedeg=np.floor(ddmm/100.)     
    themin=(ddmm-thedeg*100.)/60.     
    return thedeg+themin;                # Input is ddmm.cccc and output is dd.cccc 
newlat=ddmm.apply(ddmm2dd)              #latitude in degree decimal format

sc = ax.scatter(outbound['WIND_SPEED_TRUE'],outbound['AIR_TEMPERATURE'], c=newlat['LATITUDE'])
ax.set_xlabel("Wind Speed (m/s)")                           #Label x axis
ax.set_ylabel("Air Temperature (ºC)")                       #Label y axis
ax.set_title("Wind Speed v Air Temperature")                #Set title

cbar = fig.colorbar(sc)                             #create colorbar  
cbar.ax.get_yaxis().labelpad = 15                   #Space color bar
cbar.ax.set_ylabel('Latitude ºS', rotation=270)        #Label colorbar
fig.savefig("SCDM_P2_scat.png", dpi=200)            #Save figure in PNG with a resolution of 200 DPI
