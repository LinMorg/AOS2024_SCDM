#import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
#set min and degree format
def ddmm2dd(ddmm):
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.     
    print(thedeg+themin)
    
 #%%   
#load data
df = pd.read_csv(r'C:\Users\user\Downloads\SCDM\P1\Loc1_20081123_0653_ts_d1000.dat', delimiter='\t', skiprows=1)
print(df)

#%%
# create subplots with shared y-axis
fig, ax = plt.subplots(1, 2, sharey=True)
#plot df temp and salinity with shared y axis
ax[0].plot(df["T"], df["Depth"], color= "b")
ax[1].plot(df["Salinity(psu)"], df["Depth"], color= "r")
#x labels
ax[0].set_xlabel('Temperature in celsius')
ax[1].set_xlabel('Salinity (psu)')
#y label
ax[0].set_ylabel('Depth in meters')
#save figure
plt.savefig('P1_prt1_figure.png', dpi=200)
