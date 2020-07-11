#  ================================================================================
#  _____________________________________________________________________Clonogenics
#  ___________________________________________________________________________ver.2
#  ______________________________________________________________________23/03/2020
#  ================================================================================
#  Reads in clonogenics data from a .csv file. 
#  Takes averages over 6 well plate and calculates the SD and SEM accounting for NaN entries.
#  Calculates the plating efficiency (PE) by finding the 0 Gy controls
#  Uses the PE to calculate the Normalised Survival Fraction (NSF) for remaining doses.
#  Propagates errors throughout and plots NSF vs. Dose / Gy in a scatter plot. 
#  Currently assumed 6 doses, namely 0Gy, 0.5Gy, 1Gy, 2Gy, 4Gy, 8Gy. Will generalise further in the future. 
#  ================================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import seaborn; seaborn.set() 

data = pd.read_csv("C:/Users/User/Somewhere/CataniaDataOxic.csv")
data = data.replace('',np.nan)

seed_num=np.array(data["SEEDED"]) # creates a single row
dose=np.array(data["DOSE"])
well1=np.array(data["WELL_1"])
well2=np.array(data["WELL_2"])
well3=np.array(data["WELL_3"])
well4=np.array(data["WELL_4"])
well5=np.array(data["WELL_5"])
well6=np.array(data["WELL_6"])
length=len(well1)

seed_err=10*seed_num/100
seed_err=seed_err.reshape(1,length)
seed_num=seed_num.reshape(1,length)
dose=dose.reshape(1,length)
well1=well1.reshape(1,length) 
well2=well2.reshape(1,length)
well3=well3.reshape(1,length)
well4=well4.reshape(1,length)
well5=well5.reshape(1,length)
well6=well6.reshape(1,length)

# In hindsight the above step was unecessary and leads to additional coding. Revisit.

wells=np.vstack((well1,well2,well3,well4,well5,well6)) 
well_sums=np.zeros(length).reshape(1,length)
well_stdv=np.zeros(length).reshape(1,length)
well_SEM=np.zeros(length).reshape(1,length)
divisor=np.zeros(length)+wells.shape[0]
divisor=divisor.reshape(1,length)


for j in range(0,length):
	div=wells.shape[0]
	for i in range(0,wells.shape[0]):
		if np.isnan(wells[i,j]):
			div-=1
			divisor[0,j]=div
	summation=np.nansum(wells[:,j])
	well_sums[0,j]=summation

# In hindsight, it would have been better to just use average=np.nanmean(wells, axis=0) and not have reshaped things. Revisit this.

average=well_sums/divisor

for j in range(0,length):
	for i in range(0,wells.shape[0]):
		std=np.nanstd(wells[:,j])
		well_stdv[0,j]=std

# Same as above, well_stdv=np.nanstd(wells, axis=0) would have done the same job. 

print(data)

find_control=np.where(dose==0)
no_control=len(find_control)
find_half_gy=np.where(dose==0.5)
no_half=len(find_half_gy)
find_one_gy=np.where(dose==1)
no_one=len(find_one_gy)
find_two_gy=np.where(dose==2)
no_two=len(find_two_gy)
find_four_gy=np.where(dose==4)
no_four=len(find_four_gy)
find_eight_gy=np.where(dose==8)
no_eight=len(find_eight_gy)

well_SEM[find_control]=well_stdv[find_control]/np.sqrt(no_control)
well_SEM[find_half_gy]=well_stdv[find_half_gy]/np.sqrt(no_half)
well_SEM[find_one_gy]=well_stdv[find_one_gy]/np.sqrt(no_one)
well_SEM[find_two_gy]=well_stdv[find_two_gy]/np.sqrt(no_two)
well_SEM[find_four_gy]=well_stdv[find_four_gy]/np.sqrt(no_four)
well_SEM[find_eight_gy]=well_stdv[find_eight_gy]/np.sqrt(no_eight)

combined_mean=np.zeros(6).reshape(1,6)
combined_mean[0,0]=np.nanmean(average[find_control])
combined_mean[0,1]=np.nanmean(average[find_half_gy])
combined_mean[0,2]=np.nanmean(average[find_one_gy])
combined_mean[0,3]=np.nanmean(average[find_two_gy])
combined_mean[0,4]=np.nanmean(average[find_four_gy])
combined_mean[0,5]=np.nanmean(average[find_eight_gy])

combined_stdv=np.zeros(6).reshape(1,6)
combined_stdv[0,0]=np.nanmean(well_stdv[find_control])
combined_stdv[0,1]=np.nanmean(well_stdv[find_half_gy])
combined_stdv[0,2]=np.nanmean(well_stdv[find_one_gy])
combined_stdv[0,3]=np.nanmean(well_stdv[find_two_gy])
combined_stdv[0,4]=np.nanmean(well_stdv[find_four_gy])
combined_stdv[0,5]=np.nanmean(well_stdv[find_eight_gy])

combined_SEM=np.zeros(6).reshape(1,6)
combined_SEM[0,0]=np.nanmean(well_SEM[find_control])
combined_SEM[0,1]=np.nanmean(well_SEM[find_half_gy])
combined_SEM[0,2]=np.nanmean(well_SEM[find_one_gy])
combined_SEM[0,3]=np.nanmean(well_SEM[find_two_gy])
combined_SEM[0,4]=np.nanmean(well_SEM[find_four_gy])
combined_SEM[0,5]=np.nanmean(well_SEM[find_eight_gy])

combined_seed_num=np.zeros(6).reshape(1,6)
combined_seed_num[0,0]=np.nanmean(seed_num[find_control])
combined_seed_num[0,1]=np.nanmean(seed_num[find_half_gy])
combined_seed_num[0,2]=np.nanmean(seed_num[find_one_gy])
combined_seed_num[0,3]=np.nanmean(seed_num[find_two_gy])
combined_seed_num[0,4]=np.nanmean(seed_num[find_four_gy])
combined_seed_num[0,5]=np.nanmean(seed_num[find_eight_gy])

combined_seed_err=np.zeros(6).reshape(1,6)
combined_seed_err[0,0]=np.nanmean(seed_err[find_control])
combined_seed_err[0,1]=np.nanmean(seed_err[find_half_gy])
combined_seed_err[0,2]=np.nanmean(seed_err[find_one_gy])
combined_seed_err[0,3]=np.nanmean(seed_err[find_two_gy])
combined_seed_err[0,4]=np.nanmean(seed_err[find_four_gy])
combined_seed_err[0,5]=np.nanmean(seed_err[find_eight_gy])

combined_dose=np.zeros(6).reshape(1,6)
combined_dose[0,0]=np.nanmean(dose[find_control])
combined_dose[0,1]=np.nanmean(dose[find_half_gy])
combined_dose[0,2]=np.nanmean(dose[find_one_gy])
combined_dose[0,3]=np.nanmean(dose[find_two_gy])
combined_dose[0,4]=np.nanmean(dose[find_four_gy])
combined_dose[0,5]=np.nanmean(dose[find_eight_gy])

# Could turn a lot of the above into a for loop using f"" and {}

plating_efficiency=100*combined_mean/combined_seed_num
plating_efficiency_err=100*np.sqrt((combined_SEM/combined_mean)**2+(combined_seed_err/combined_seed_num)**2)*plating_efficiency

survival_frac=combined_mean/(combined_seed_num*plating_efficiency[0,0])

survival_frac_err=np.sqrt(((np.sqrt((combined_seed_err/combined_seed_num)**2+(plating_efficiency_err[0,0]/plating_efficiency[0,0])**2))/(combined_seed_num*plating_efficiency[0,0]))**2+(combined_SEM/combined_mean)**2)*(combined_mean/(combined_seed_num*plating_efficiency[0,0]))


survival_frac_norm=np.zeros(6)
survival_frac_norm_err=np.zeros(6)
for i in range(0,6):
	survival_frac_norm[i]=survival_frac[0,i]/survival_frac[0,0]
	survival_frac_norm_err[i]=np.sqrt((survival_frac_err[0,i]/survival_frac[0,i])**2+(survival_frac_err[0,0]/survival_frac[0,0])**2)*(survival_frac[0,i]/survival_frac[0,0])

x=np.zeros(6)
y=np.zeros(6)
erry=np.zeros(6)
errx=np.zeros(6)
for i in range(0,6):
	y[i]=survival_frac_norm[i]
	x[i]=combined_dose[0,i]
	erry[i]=survival_frac_norm_err[i]
	errx[i]=combined_dose[0,i]/40
# the above loop is an unfortunate necessity as a result of having reshaped in the begining. Revisit this. 

plt.yscale('log')
plt.errorbar(x, y, yerr=erry,xerr=errx, fmt='.')
plt.grid(b=True, which='major', color='grey', linestyle='-', linewidth='0.1')
plt.grid(b=True, which='minor', color='grey', linestyle='--', linewidth='0.1')
plt.xlabel('Dose /Gy', fontsize=16)
plt.ylabel('Normalised Survival Fraction', fontsize=16)
plt.title('2D Oxic E2 Cells - Catania 30MeV Protons',fontsize=20)
plt.show()