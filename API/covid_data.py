# need to download these libraries before running
from uk_covid19 import Cov19API
import pandas as pd

def retrieve_columns(data):
	# function to get the names of columns and return them as a list
	columns=[]
	for col in data.columns:
		columns.append(col)
	return columns

def moving_average(dataSet,columnTitle,units,population):
	# function to calculate moving averages (mid-point)
	data=dataSet[columnTitle].rolling(window=7, center=True).mean()*units/(population)
	return data 

def moving_average_combine(data_set,nation_list,columns_list,pops_list,units,column_number):
	# function to calculate the 7 day averages for each region and put them into the data base
	strings=[]
	for i in range(0, len(nation_list)):
		values=moving_average(data_set.loc[data_set['Nation']==nation_list[i]],columns_list[column_number],units, pops_list[i])
		values.fillna('')
		strings.append('%s (7 day moving average) %s' % (columns_list[column_number], nation_list[i]))
		data_set.insert(i, strings[i], values, allow_duplicates=False)
	new_columns=retrieve_columns(data_set)
	valuesnew=data_set[new_columns[0]].combine_first(data_set[new_columns[1]]).combine_first(data_set[new_columns[2]]).combine_first(data_set[new_columns[3]])
	data_set.insert(1, '%s (7 day moving average) per million population' % columns_list[column_number], valuesnew, allow_duplicates=False)
	for i in range(0, len(nation_list)):
		data_set.drop(columns=[strings[i]], inplace=True)

def main():
	# Built from documentation: https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/pages/getting_started.html
  # performs api call
	all_nations = ["areaType=nation"]
	cases_and_deaths = {
		"Date": "date",
		"Nation": "areaName",
		# Cases
		"Daily cases by publish date": "newCasesBySpecimenDate",
		"Cumulative cases by publish date": "cumCasesBySpecimenDate",
		# Deaths
		"Daily deaths within 28 days of positive test by death date": "newDeaths28DaysByDeathDate",
		"Cumulative deaths within 28 days of positive test by death date": "cumDeaths28DaysByDeathDate",
		# Vaccinations
		"Daily people who have received 1st dose vaccinations, by report date" : "newPeopleVaccinatedFirstDoseByPublishDate",
		"Cumulative people who have received 1st dose vaccinations, by report date" : "cumPeopleVaccinatedFirstDoseByPublishDate",
		"Daily people who have received 2nd dose vaccinations, by report date" : "newPeopleVaccinatedSecondDoseByPublishDate",
		"Cumulative people who have received 2nd dose vaccinations, by report date" : "cumPeopleVaccinatedSecondDoseByPublishDate",
		"Daily people who have received 3rd dose vaccinations, by report date":"newPeopleVaccinatedThirdDoseByPublishDate",
		"Cumulative people who have received 3rd dose vaccinations, by report date":"cumPeopleVaccinatedThirdDoseByPublishDate",
		"Daily people people who have received booster or 3rd dose vaccinations, by report date" : "newPeopleVaccinatedThirdInjectionByPublishDate",
		"Cumulative people people who have received booster or 3rd dose vaccinations, by report date" : "cumPeopleVaccinatedThirdInjectionByPublishDate",
		# Testing
		"Daily pillar one tests by publish date":"newPillarOneTestsByPublishDate",
		"Cumulative pillar one tests by publish date":"cumPillarOneTestsByPublishDate",
		"Daily pillar two tests by publish date":"newPillarTwoTestsByPublishDate",
		"Cumulative pillar two tests by publish date":"cumPillarTwoTestsByPublishDate",
		"Daily tests (all pillars) by publish date":"newPillarOneTwoTestsByPublishDate",
		"Cumulative tests (all pillars) by publish date":"cumPillarOneTwoTestsByPublishDate",
		# Healthcare
		"Daily patients in hospital":"hospitalCases",
		"Daily patients in mechanical ventilation beds":"covidOccupiedMVBeds",
		"Daily patients admitted to hospital":"newAdmissions",
		"Cumulative patients admitted to hospital":"cumAdmissions",
	}

	api = Cov19API(
		filters=all_nations,
		structure=cases_and_deaths
	)

	data = api.get_dataframe()

	columns=retrieve_columns(data) # Getting column titles
	nations=data['Nation'].unique() # Getting nation names
	nation_pops=[56550138,1895510,5466000,3169586] # Making a list of the populations

	average_columns=[] # An index of the columns which need daily averages
	average_columns=[i for i in range(2,20,2)] 
	average_columns.append(20)
	average_columns.append(21)
	average_columns.append(22)

	for number in average_columns: # Calculate all the daily averages
		moving_average_combine(data, nations, columns,nation_pops,1000000,number)

	data.to_csv('C:/Users/Aaron/OneDrive/Documents/assembly/covid_dashboards/all_covid_data.csv') # Export to csv

if __name__ == "__main__":
	main()
