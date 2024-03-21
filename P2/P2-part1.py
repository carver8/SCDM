import pandas as pd
import matplotlib.pyplot as plt
ctd = pd.read_csv('CTD-20081129-0652-DTS.dat', sep='\t')

fig, ax = plt.subplots(1, 2, sharey=True)   #Define figure with two subplots 1 row two columns
ax[0].set_title("Temperature v. Depth") #Set subplot1 title
ax[0].plot(ctd["T"], ctd["Depth"], color = 'b')     #Plot Temp vs Depth on subplot1
ax[0].set_ylabel("Depth (m)")           #Label y axis
ax[0].set_xlabel("Temperature (ºC)")    #Label x axis for Temp
ax[0].grid(True)                        #Turn on grid for subplot 1

ax[1].set_title("Salinity v. Depth")    #Set subplot2 title
ax[1].plot(ctd["Salinity(cpu)"],ctd["Depth"], color = 'r')  #Plot Salinity vs Depth on subplot2
ax[1].set_xlabel("Salinity (cpu)")      #Label x axis for salinity
ax[1].grid(True)                        #Turn on grid for subplot 2

plt.gca().invert_yaxis()    #Invert y axis so greater depth is visually lower on y axis
plt.show()                  #Show plot figure
fig.savefig("SCDM_P1_twopanel.png")   