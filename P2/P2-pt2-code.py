#import packages
import pandas as pd
import matplotlib.pyplot as plt

#load data and set index
df = pd.read_csv(r'C:\Users\user\Downloads\SCDM\P2\Prt02\SAA2_WC_2017_metocean_10min_avg.csv', delimiter= ',', na_values=['', '-', 'NA'])
df.set_index('TIME_SERVER')
print(df.head())

#%%
#splicing df for depature to 4 july
df2= df.iloc[0:905]
print(df2.head())
print(df2.columns)
labels= df2["TIME_SERVER"]

#%%
# #plot timeseries of temp
plt.style.use('grayscale')
fig, ax = plt.subplots()
fig, ax = plt.subplots()
ax.plot(df2["TIME_SERVER"], df2["TSG_TEMP"])

ax.set_xticklabels(df2.TIME_SERVER, rotation=90)
ax.set_xticks(labels[::100])
ax.set_xticklabels(labels[::100], rotation=90)

ax.set_ylabel("Temperature (°C)")
ax.set_xlabel("Date")
plt.savefig('P2_prt2_timeseriesfigv1.png')

#%%
# # #plot histogram salinity
plt.style.use("default")
fig, ax = plt.subplots()
ax.hist(df2['TSG_SALINITY'], label= "Salinity (psu)", bins= 10, range=(30, 35))
ax.set_xlabel("Salinity (psu)")
ax.set_ylabel(('# of Observations'))
plt.savefig('P2_prt2_histfig.png', dpi=200)

#%%
# # #plot scatterplot wind speed against TEMP
plt.style.use('default')
fig, ax = plt.subplots()
ax.scatter(df2['WIND_SPEED_TRUE'], df2['TSG_TEMP'],  c= df2.LATITUDE)
ax.set_xlabel('Wind speed meter/sec')
ax.set_ylabel('Temperature (°C)')
ax.set_label('Scatter plot of wind speed against temperature')
plt.colorbar(ax.scatter(df2['WIND_SPEED_TRUE'], df2['TSG_TEMP'],  c= df2.LATITUDE), label="Latitude")
plt.savefig('P2_prt2_scatterfig.png', dpi=200)

