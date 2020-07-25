#  ================================================================================.
#  _____________________________________________________________________Clonogenics.
#  ___________________________________________________________________________ver.4.
#  ______________________________________________________________________23/03/2020.
#  ================================================================================.
#  Reads in clonogenics data from a .csv file. 
#  Finds the number of unique doses and their frequency of occurence.
#  Takes average count, standard deviation and SEM of each 6 well plate and calculates accounting for NaN entries.
#  Averages over replicates. 
#  Calculates the plating efficiency (PE) and associated error via error propagation. 
#  Uses the PE to calculate the Normalised Survival Fraction (NSF) and associated error via error propagation. 
#  Plots NSF vs. Dose / Gy in a scatter plot and fits curve using non-linear regression. 
#  Returns alpha and beta values with standard deviation calculated via covariance diagonal.
#  Generalised for messy data. As long as the input data columns are of the form provided in the mock example csv it should work. Ordering of data by dose before application not necessary.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import seaborn; seaborn.set() 
import scipy

def SFmodel(dose,alpha,beta,):
	expterm=(-1)*((alpha*dose)+(beta*dose**2))
	SF = np.exp(expterm)
	return SF

#  The above function describes the linear quadratic model of cell survival. Used in curve fitting. 

def main(): 
	data = pd.read_csv("C:/Users/User/LocationOfCsvFiles/CataniaDataOxic.csv")
	data = data.replace('',np.nan)

	seed_num=np.array(data["SEEDED"]) 
	seed_err=2*seed_num/100
	dose=np.array(data["DOSE"])
	dose_err=10*dose/100
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

	non_nan_entries=[]
	for i in range(0,length):
		non_nan_entries.append(np.count_nonzero(~np.isnan(wells[:,i])))

#  Counts the number of non-NaN entries in a row, useful for calculating the SEM which requires stdv/sqrt(observations)

	well_SEM=well_stdv/np.sqrt(non_nan_entries)

#  Calculates the SEM for each 6 well plate.

	unique_dose_array_count=np.array([np.unique(dose, return_counts=True)])
	unique_dose_array=unique_dose_array_count[0,0,:]
	unique_dose_array_count=unique_dose_array_count[0,1,:]
#  Returns an array containing the unique doses and an array containing the number of times they appear.

	var_holder = {}
	indexer= {}
	for i in range(0,len(unique_dose_array)):
		var_holder['find_' + str(i)] =np.array([np.where(dose==unique_dose_array[i])])
	locals().update(var_holder)

#  The above produces new variables "find_n" which will act as mask arrays to be input as indexes to pin point relevent data. For instance average[find_0] would produces the elements of "average" array which correspond to 0 Gy.   

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
	plating_efficiency_err=plating_efficiency*np.sqrt((combined_SEM/combined_mean)**2+(combined_seed_err/combined_seed_num)**2)

#  Calculates plating efficiency and associated error via error propagation. 

	survival_frac=combined_mean/(combined_seed_num*plating_efficiency[0])

	survival_frac_err=np.sqrt((combined_seed_err/combined_seed_num)**2+(plating_efficiency_err[0]/plating_efficiency[0])**2+(combined_SEM/combined_mean)**2)*survival_frac

#  Calculates survival fractions and associated error via error propagation. 

	survival_frac_norm=np.zeros(unique_dose_array.size)
	survival_frac_norm_err=np.zeros(unique_dose_array.size)
	for i in range(0,unique_dose_array.size):
		survival_frac_norm[i]=survival_frac[i]/survival_frac[0]
		survival_frac_norm_err[i]=np.sqrt((survival_frac_err[i]/survival_frac[i])**2+(survival_frac_err[0]/survival_frac[0])**2)*survival_frac_norm[i]

#  Calculates normalised survival fractions and associated error via error propagation.

	g=[0.4861,0.01947]

	ng,cov=scipy.optimize.curve_fit(SFmodel,combined_dose,survival_frac_norm,g,sigma=survival_frac_norm_err, bounds=(0,np.inf),method="trf")

	n=len(combined_dose)

	y=np.empty(n)

	for i in range(n):
		y[i]=SFmodel(combined_dose[i],ng[0],ng[1])
		print(y[i])

	stdevs=np.sqrt(np.diag(cov))

	plt.yscale('log')
	plt.errorbar(combined_dose, survival_frac_norm, yerr=survival_frac_norm_err,xerr=combined_dose_err, fmt='.')
	plt.grid(b=True, which='major', color='grey', linestyle='-', linewidth='0.1')
	plt.grid(b=True, which='minor', color='grey', linestyle='--', linewidth='0.1')
	plt.xlabel('Dose /Gy', fontsize=16)
	plt.ylabel('Normalised Survival Fraction', fontsize=16)
	plt.title('2D Oxic E2 Cells - Catania 30MeV Protons',fontsize=20)
	plt.plot(combined_dose, y, 'r-')
	plt.show()

#  Plots the data and the fit curve given some initial guess "g"

	appender=np.zeros(len(combined_dose)-2)
	newng=np.append(ng,appender)
	newstdevs=np.append(stdevs,appender)

	newdata={"Dose Gy": combined_dose, "Error": combined_dose_err, "NSF": survival_frac_norm, "Error": survival_frac_norm_err, "Alpha/Beta": newng, "Stdv": newstdevs}
	newdataframe=pd.DataFrame(data=newdata)

	output=newdataframe.to_csv("SurvivalData.csv")

#  Sends the data to a new .csv file

if __name__ == "__main__":
	main()
