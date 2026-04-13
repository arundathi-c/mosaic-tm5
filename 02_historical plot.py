from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import glob
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

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_oct.nc')
cesmamip_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_nov.nc')
cesmamip_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_dec.nc')
cesmamip_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_jan.nc')
cesmamip_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_feb.nc')
cesmamip_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_mar.nc')
cesmamip_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_apr.nc')
cesmamip_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_may.nc')
cesmamip_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_jun.nc')
cesmamip_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_jul.nc')
cesmamip_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_aug.nc')
cesmamip_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/MIROC-ES2H-monthly/conccn_Emon_MIROC-ES2H_historical_r1i1p4f2_gn_sep.nc')
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

ds1 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_oct.nc')
mriamip_oct= np.reshape((ds1.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds2 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_nov.nc')
mriamip_nov = np.reshape((ds2.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds3 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_dec.nc')
mriamip_dec = np.reshape((ds3.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds4 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_jan.nc')
mriamip_jan = np.reshape((ds4.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds5 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_feb.nc')
mriamip_feb = np.reshape((ds5.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds6 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_mar.nc')
mriamip_mar = np.reshape((ds6.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds7 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_apr.nc')
mriamip_apr = np.reshape((ds7.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds8 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_may.nc')
mriamip_may = np.reshape((ds8.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds9 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_jun.nc')
mriamip_jun = np.reshape((ds9.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds10 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_jul.nc')
mriamip_jul = np.reshape((ds10.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds11 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_aug.nc')
mriamip_aug = np.reshape((ds11.variables['conccn'][:,0]),newshape=-1)*10**(-6)
ds12 = Dataset('/home/chandras/mosaic-paper/cmip6/UKESM1-0-LL-monthly/conccn_Emon_UKESM1-0-LL_historical_r1i1p1f2_gn_sep.nc')
mriamip_sep = np.reshape((ds12.variables['conccn'][:,0]),newshape=-1)*10**(-6)
mriamip=[mriamip_oct,mriamip_nov,mriamip_dec,mriamip_jan,mriamip_feb,mriamip_mar,mriamip_apr,mriamip_may,mriamip_jun,mriamip_jul,mriamip_aug,mriamip_sep]
months = [10,11,12,1,2,3,4,5,6,7,8,9]
basecase_ds = xr.open_dataset('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/basecase_dailypath.nc')
tm5_ds =  [basecase_ds.groupby('time.month')[i]['conccn'].to_numpy() for i in months]
tm5_monmean = [np.mean(basecase_ds['conccn'].where(basecase_ds['time'].dt.month == months[i])) for i in range(0,12)]

bulkmsa = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/bulkmsa_dailypath.nc')
so4nucl = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/so4nucl_dailypath.nc')
dmshigh = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/dmshigh_dailypath.nc')
dmslow = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/dmslow_dailypath.nc')
msaelvoc = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/msaelvoc_dailypath.nc')
msasvoc = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/msasvoc_dailypath.nc')
nuclhigh = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/nuclhigh_dailypath.nc')
nucllow = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/nucllow_dailypath.nc')
sshigh = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/sshigh_dailypath.nc')
sslow = glob.glob('/home/chandras/mosaic-paper/sensitivityanalysis/dailypath/sslow_dailypath.nc')

def month_avg(filename):
    ds = xr.open_dataset(filename[0])
    ds = ds.sel(time = slice('01-01-2019',None))
    ds = ds.resample(time = '1ME').mean()
    
    '''ds = ds.mean(dim = 'ncells')
    for i in range(1,12):
        temp = xr.open_dataset(filename[i])
        temp  = temp.mean(dim = 'ncells')
        ds = xr.combine_by_coords([ds,temp])'''
    return(ds)

bulkmsa_ds = month_avg(bulkmsa)
basecase_nonucl_ds = month_avg(so4nucl)
dmshigh_ds = month_avg(dmshigh)
dmslow_ds = month_avg(dmslow)
msaelvoc_ds = month_avg(msaelvoc)
msasvoc_ds = month_avg(msasvoc)
nuclhigh_ds = month_avg(nuclhigh)
nucllow_ds = month_avg(nucllow)
sshigh_ds = month_avg(sshigh)
sslow_ds = month_avg(sslow)


timeline = np.arange(1,48,4)
color = ['#1b9e77','#66a61e','#d95f02','#7570b3','#e7298a','#e6ab02']
#cesmhist_pos = np.arange(2,61,5)
#cesmamip_pos = np.arange(4,61,5)
#mrihist_pos = np.arange(3,61,5)
#mriamip_pos = np.arange(5,64,5)

fig,ax = plt.subplots(figsize = (20,12))
bx1 = ax.violinplot(cesmhist,positions=timeline,showmedians=True)#
for pc in bx1['bodies']:
    pc.set_color(color[0])#,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx1['cmedians'].set_color(color[0])
bx1['cbars'].set_color(color[0])
bx1['cmins'].set_color(color[0])
bx1['cmaxes'].set_color(color[0])
bx2 = ax.violinplot(cesmamip,positions=timeline+2,showmedians=True)#,
for pc in bx2['bodies']:
    pc.set_color(color[1]) #,medianprops = dict(color = "black"),flierprops=dict(marker="."))
bx2['cmedians'].set_color(color[1])
bx2['cbars'].set_color(color[1])
bx2['cmins'].set_color(color[1])
bx2['cmaxes'].set_color(color[1])
bx3 = ax.violinplot(mrihist,positions=timeline+1,showmedians=True)
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
bx5 = tm5 = ax.violinplot(tm5_ds,positions = timeline+4,showmedians=True)
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
print(tm5_monmean)
plot1 = plt.scatter(timeline+1.5,tm5_monmean, color = color[4], marker = '*',s = 200)#,linestyles='dashed')

plot2 = plt.scatter(timeline+1.5,bulkmsa_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,basecase_nonucl_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,dmshigh_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,dmslow_ds.conccn, color = color[4], marker = 'x')    
#plt.scatter(timeline+1.5,msaelvoc_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,msasvoc_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,nuclhigh_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,nucllow_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,sshigh_ds.conccn, color = color[4], marker = 'x')
#plt.scatter(timeline+1.5,sslow_ds.conccn, color = color[4], marker = 'x')
#ax.legend([bx1, bx3,bx2,bx4], ['CESM2(hist)', 'MRIESM2(hist)','MIROC-ES2H(hist)','UKESM1(hist)'], loc='upper left')
ax.legend([bx1['bodies'][0], bx3['bodies'][0],bx2['bodies'][0],bx4['bodies'][0],plot,plot2,plot1], ['CESM2(hist)', 'MRIESM2(hist)','MIROC-ES2H(hist)','UKESM1(hist)','MOSAIC','TM5 BULKMSA','TM5 BASECASE'], loc='upper left',fontsize = 20)
plt.ylabel('Number Concentration (cm⁻³)',fontsize = 20)
plt.xlabel('Month - Year',fontsize = 20)
ax.set_xlim(0.5,48.5)
ax.set_ylim(0)
#plt.grid()
plt.tight_layout()
#plt.show()
plt.savefig('/home/chandras/mosaic-paper/figures/hist-cmip6-violin-type2.svg',dpi = 300)
