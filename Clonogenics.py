#  ================================================================================.
#  _____________________________________________________________________Clonogenics.
#  ___________________________________________________________________________ver.3.
#  ______________________________________________________________________23/03/2020.
#  ================================================================================.
#  Reads in clonogenics data from a .csv file. 
#  Finds the number of unique doses and their individual frequency of occurence.
#  Takes averages over 6 well plate and calculates the SD and SEM accounting for NaN entries.
#  Averages over replicates. 
#  Calculates the plating efficiency (PE) and associated error. 
#  Uses the PE to calculate the Normalised Survival Fraction (NSF).
#  Propagates errors throughout and plots NSF vs. Dose / Gy in a scatter plot. 
#  Generalised so that it doesn't need to take specific doses. Useful if you need to investigate smaller dose intervals and have a lot of doses. 
#  ================================================================================.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import seaborn; seaborn.set() 

data = pd.read_csv("C:/Users/User/Place/CataniaDataOxic.csv")
data = data.replace('',np.nan)

seed_num=np.array(data["SEEDED"]) 
seed_err=seed_num/10
dose=np.array(data["DOSE"])
dose_err=dose/10
well1=np.array(data["WELL_1"])
well2=np.array(data["WELL_2"])
well3=np.array(data["WELL_3"])
well4=np.array(data["WELL_4"])
well5=np.array(data["WELL_5"])
well6=np.array(data["WELL_6"])
length=len(well1)

wells=np.vstack((well1,well2,well3,well4,well5,well6)) 

average=np.nanmean(wells, axis=0)

well_stdv=np.nanstd(wells, axis=0)

well_SEM=np.zeros(length)

unique_dose_array_count=np.array([np.unique(dose, return_counts=True)])
unique_dose_array=unique_dose_array_count[0,0,:]
unique_dose_array_count=unique_dose_array_count[0,1,:]

#  Returns an array containing the unique doses and an array containing the number of times they appear.

var_holder = {}
indexer= {}
for i in range(0,len(unique_dose_array)):
	var_holder['find_' + str(i)] =np.array([np.where(dose==unique_dose_array[i])])
locals().update(var_holder)

for i in range(0,unique_dose_array.size):
	well_SEM[var_holder['find_' + str(i)]]=well_stdv[var_holder['find_' + str(i)]]/np.sqrt(var_holder['find_' + str(i)].size)

combined_mean=np.zeros(unique_dose_array.size)
combined_stdv=np.zeros(unique_dose_array.size)
combined_SEM=np.zeros(unique_dose_array.size)
combined_seed_num=np.zeros(unique_dose_array.size)
combined_seed_err=np.zeros(unique_dose_array.size)
combined_dose=np.zeros(unique_dose_array.size)
combined_dose_err=np.zeros(unique_dose_array.size)

for i in range(0,unique_dose_array.size):
	combined_mean[i]=np.nanmean(average[var_holder['find_' + str(i)]])
	combined_stdv[i]=np.nanmean(well_stdv[var_holder['find_' + str(i)]])
	combined_SEM[i]=np.nanmean(well_SEM[var_holder['find_' + str(i)]])
	combined_seed_num[i]=np.nanmean(seed_num[var_holder['find_' + str(i)]])
	combined_seed_err[i]=np.nanmean(seed_err[var_holder['find_' + str(i)]])
	combined_dose[i]=np.nanmean(dose[var_holder['find_' + str(i)]])
	combined_dose_err[i]=np.nanmean(dose_err[var_holder['find_' + str(i)]])

#  Averages the replicates.

plating_efficiency=100*combined_mean/combined_seed_num
plating_efficiency_err=100*np.sqrt((combined_SEM/combined_mean)**2+(combined_seed_err/combined_seed_num)**2)*plating_efficiency

#  Calculates plating efficiency and associated error via error propagation. 

survival_frac=combined_mean/(combined_seed_num*plating_efficiency[0])

survival_frac_err=np.sqrt(((np.sqrt((combined_seed_err/combined_seed_num)**2+(plating_efficiency_err[0]/plating_efficiency[0])**2))/(combined_seed_num*plating_efficiency[0]))**2+(combined_SEM/combined_mean)**2)*(combined_mean/(combined_seed_num*plating_efficiency[0]))

#  Calculates survival fractions and associated error via error propagation. 

survival_frac_norm=np.zeros(unique_dose_array.size)
survival_frac_norm_err=np.zeros(unique_dose_array.size)
for i in range(0,unique_dose_array.size):
	survival_frac_norm[i]=survival_frac[i]/survival_frac[0]
	survival_frac_norm_err[i]=np.sqrt((survival_frac_err[i]/survival_frac[i])**2+(survival_frac_err[0]/survival_frac[0])**2)*(survival_frac[i]/survival_frac[0])

#  Calculates normalised survival fractions and associated errorvia error propagation.

plt.yscale('log')
plt.errorbar(combined_dose, survival_frac_norm, yerr=survival_frac_norm_err,xerr=combined_dose_err, fmt='.')
plt.grid(b=True, which='major', color='grey', linestyle='-', linewidth='0.1')
plt.grid(b=True, which='minor', color='grey', linestyle='--', linewidth='0.1')
plt.xlabel('Dose /Gy', fontsize=16)
plt.ylabel('Normalised Survival Fraction', fontsize=16)
plt.title('2D Oxic E2 Cells - Catania 30MeV Protons',fontsize=20)
plt.show()
