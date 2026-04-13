from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_oct.nc')
cesmhist_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_nov.nc')
cesmhist_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_dec.nc')
cesmhist_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_jan.nc')
cesmhist_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_feb.nc')
cesmhist_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_mar.nc')
cesmhist_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_apr.nc')
cesmhist_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_may.nc')
cesmhist_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_jun.nc')
cesmhist_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_jul.nc')
cesmhist_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_aug.nc')
cesmhist_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_historical/conccn_Emon_CESM2_historical_r10i1p1f1_gn_sep.nc')
cesmhist_sep = np.reshape((ds12.variables['conccn'][:,0]),newshape=-1)*10**(-6)
cesmhist=[cesmhist_oct,cesmhist_nov,cesmhist_dec,cesmhist_jan,cesmhist_feb,cesmhist_mar,cesmhist_apr,cesmhist_may,cesmhist_jun,cesmhist_jul,cesmhist_aug,cesmhist_sep]

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_oct.nc')
cesmamip_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_nov.nc')
cesmamip_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_dec.nc')
cesmamip_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_jan.nc')
cesmamip_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_feb.nc')
cesmamip_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_mar.nc')
cesmamip_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_apr.nc')
cesmamip_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_may.nc')
cesmamip_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_jun.nc')
cesmamip_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_jul.nc')
cesmamip_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_aug.nc')
cesmamip_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/cesm2_amip/conccn_Emon_CESM2_amip_r10i1p1f1_gn_sep.nc')
cesmamip_sep = np.reshape((ds12.variables['conccn'][:,0]),newshape=-1)*10**(-6)
cesmamip=[cesmamip_oct,cesmamip_nov,cesmamip_dec,cesmamip_jan,cesmamip_feb,cesmamip_mar,cesmamip_apr,cesmamip_may,cesmamip_jun,cesmamip_jul,cesmamip_aug,cesmamip_sep]

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_oct.nc')
mrihist_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_nov.nc')
mrihist_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_dec.nc')
mrihist_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_jan.nc')
mrihist_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_feb.nc')
mrihist_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_mar.nc')
mrihist_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_apr.nc')
mrihist_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_may.nc')
mrihist_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_jun.nc')
mrihist_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_jul.nc')
mrihist_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_aug.nc')
mrihist_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_historical/conccn_Emon_MRI-ESM2-0_historical_r1i1p1f1_gn_sep.nc')
mrihist_sep = np.reshape((ds12.variables['conccn'][:,0]),newshape=-1)*10**(-6)
mrihist=[mrihist_oct,mrihist_nov,mrihist_dec,mrihist_jan,mrihist_feb,mrihist_mar,mrihist_apr,mrihist_may,mrihist_jun,mrihist_jul,mrihist_aug,mrihist_sep]

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_oct.nc')
mriamip_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_nov.nc')
mriamip_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_dec.nc')
mriamip_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_jan.nc')
mriamip_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_feb.nc')
mriamip_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_mar.nc')
mriamip_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_apr.nc')
mriamip_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_may.nc')
mriamip_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_jun.nc')
mriamip_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_jul.nc')
mriamip_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_aug.nc')
mriamip_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/hist_amip_comp/mriesm2_amip/conccn_Emon_MRI-ESM2-0_amip_r1i1p1f1_gn_sep.nc')
mriamip_sep = np.reshape((ds12.variables['conccn'][:,0]),newshape=-1)*10**(-6)
mriamip=[mriamip_oct,mriamip_nov,mriamip_dec,mriamip_jan,mriamip_feb,mriamip_mar,mriamip_apr,mriamip_may,mriamip_jun,mriamip_jul,mriamip_aug,mriamip_sep]



months = [10,11,12,1,2,3,4,5,6,7,8,9]
basecase_ds = xr.open_dataset('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/basecase_dailypath.nc')
tm5_ds =  [basecase_ds.groupby('time.month')[i]['conccn'].to_numpy() for i in months]
tm5_monmean = [np.mean(basecase_ds['conccn'].where(basecase_ds['time'].dt.month == months[i])) for i in range(0,12) ]

timeline = np.arange(1,48,4)
color = ['#1b9e77','#66a61e','#d95f02','#7570b3','#e7298a','#e6ab02']

fig,ax = plt.subplots(figsize = (20,12))
bx1 = ax.violinplot(cesmhist,positions=timeline,showmedians=True)#
for pc in bx1['bodies']:
    pc.set_color(color[0])#,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx1['cmedians'].set_color(color[0])
bx1['cbars'].set_color(color[0])
bx1['cmins'].set_color(color[0])
bx1['cmaxes'].set_color(color[0])
bx2 = ax.violinplot(cesmamip,positions=timeline+1,showmedians=True)#,
for pc in bx2['bodies']:
    pc.set_color(color[1]) #,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx2['cmedians'].set_color(color[1])
bx2['cbars'].set_color(color[1])
bx2['cmins'].set_color(color[1])
bx2['cmaxes'].set_color(color[1])
bx3 = ax.violinplot(mrihist,positions=timeline+2,showmedians=True)
for pc in bx3['bodies']:
    pc.set_color(color[2])#,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx3['cmedians'].set_color(color[2])
bx3['cbars'].set_color(color[2])
bx3['cmins'].set_color(color[2])
bx3['cmaxes'].set_color(color[2])
bx4 = ax.violinplot(mriamip,positions=timeline+3,showmedians=True)
for pc in bx4['bodies']:
    pc.set_color(color[3])#,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx4['cmedians'].set_color(color[3])
bx4['cbars'].set_color(color[3])
bx4['cmins'].set_color(color[3])
bx4['cmaxes'].set_color(color[3])

'''
bx5 = tm5 = ax.violinplot(tm5_ds,positions = timeline+4,showmedians=True,widths=0.75)
for pc in bx5['bodies']:
    pc.set_color(color[4])#,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx5['cmedians'].set_color(color[4])
bx5['cbars'].set_color(color[4])
bx5['cmins'].set_color(color[4])
bx5['cmaxes'].set_color(color[4])
'''
def monthly_file(filename,skip_line_no,pollution,var):
    df = pd.read_csv(filename,skiprows=skip_line_no,sep='\t')
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df= df.where(df['Date/Time'] < '2020-10-01')
    df = df.drop(['Event'],axis = 1)
    df = df[df[pollution] != 1]
    df = df.resample('1D',on = 'Date/Time').mean()
    df = df.dropna()
    print(df)
    #df.set_index('Date/Time', inplace=True)
    #df = df.groupby(pd.Grouper(key='Date/Time', freq='M',group_keys = True))
    return(df)
mosaic_obs= monthly_file('/home/chandras/mosaic-paper/cpc3025_pollution_flag_1min(1).tab',43,'Flag','CP_conc [#/cm**3]')
mosaic_obs = mosaic_obs.reset_index()

xvals = timeline+1.5
xlabels = [ 'Oct \n 2019', 'Nov \n 2019', 'Dec \n 2019', 'Jan \n 2020', 'Feb \n 2020', 'Mar \n 2020', 'Apr \n 2020', 'May \n 2020', 'Jun \n 2020', 'Jul \n 2020', 'Aug \n 2020', 'Sep \n 2020']
ax.set_xticks(xvals)
ax.set_xticklabels(xlabels,fontsize = 20)
plt.yticks(fontsize = 20)
obs_ds = [mosaic_obs['CP_conc [#/cm**3]'].where(mosaic_obs['Date/Time'].dt.month == months[i]).dropna() for i in range(0,12)]
obs_median = [np.mean(mosaic_obs['CP_conc [#/cm**3]'].where(mosaic_obs['Date/Time'].dt.month == months[i]).dropna()) for i in range(0,12)]
obs_max = [np.percentile(mosaic_obs['CP_conc [#/cm**3]'].where(mosaic_obs['Date/Time'].dt.month == months[i]).dropna(),90) for i in range(0,12)]
obs_min = [np.percentile(mosaic_obs['CP_conc [#/cm**3]'].where(mosaic_obs['Date/Time'].dt.month == months[i]).dropna(),10) for i in range(0,12)]

plot = plt.hlines(obs_median, timeline,timeline+3,colors = 'k')#,linestyles='dashed')
#plot1 = plt.hlines(tm5_filtered,timeline,timeline+4,colors='r')#,linestyles='dashed')
for i in range(1,48,4):
    plt.fill_between([i,i+3] ,obs_min[i//4],obs_max[i//4] ,color= 'k', alpha=0.1)

plot1 = plt.hlines(tm5_monmean, timeline,timeline+3,colors = color[4])

ax.legend([bx1["bodies"][0], bx2["bodies"][0],bx3["bodies"][0],bx4["bodies"][0],plot1,plot], ['CESM2(hist)', 'CESM2(amip)','MRIESM2(hist)','MRIESM2(amip)','TM5','MOSAIC'], loc='upper left',fontsize = 20)
plt.ylabel('Number Concentration (cm⁻³)',fontsize = 20)
plt.xlabel('Month - Year',fontsize = 20)
plt.tight_layout()
#plt.ylim(0,1500)
plt.show()
#plt.savefig('/home/chandras/mosaic-paper/figures/amip-hist-alt.jpg',dpi = 300)
