# Libraries
import requests
import json
import csv
import pandas as pd
import re
from datetime import datetime

# Classes for exception handling

class Error(Exception):
	"""Base class for other exceptions"""
	pass
class TooLong(Error):
	"""Raised when input value length exceeds limit"""
	pass
class TooShort(Error):
	"""Raised when input value length less than or equal to 1"""
	pass
class InvalidEntry(Error):
	"""Raised when input doesn't match dd/mm/yyyy format"""
	pass
class ValueNotGender(Error):
	"""Raised when input value not M or F"""
	pass
class StrError(Error):
	"""Raised when input is not a string"""
	pass

def welcome():
	print("_______________________")
	print("A Py I...............v1")
	print("_______________________ \n")
	print("This tool is designed to search and retrieve datasets available at: https://data.nisra.gov.uk/")
	print("Please use responsibly, as a general rule, more than 30 API calls in a minute is too many.")
	print("Excessive requests can lead to HTTP error 429 - too many requests. \n")

def menu():
	print("_______________________")
	print("MENU")
	print("_______________________ \n")
	print("1. Retrieve list of datasets and download .csv files")
	print("2. Quit \n")
	'''user input for menu selection with validation'''
	while True:
		try:
			menu_num=int(input("\n Enter choice: "))
			if menu_num<=0:
				raise InvalidEntry
			elif menu_num>2:
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid number: ")
		except ValueError:
			print("\n Please enter a valid number: ")
	return menu_num

def user_input():
	""" User input for datasearch"""
	#is_valid=False
	#while not is_valid:
	#	user_in = str(input("\n Retrieve a dataframe containing datasets updated since a user specified date (YYYY/MM/DD): "))
	#	try: 
	#		inp_check = datetime.strptime(user_in, "%Y-%m-%d")
	#		is_valid=True
	#	except:
	#		print("\n Please try again. Type Date in YYYY/MM/DD format.")
	#url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadCollection/{}/en'.format(user_in)
	url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadCollection/2000-01-01/en'
	return url

def recently_updated_datasets(inpURL):
	""" Get the data at the specified URL"""
	response=requests.get(inpURL)

	""" Write response text to a JSON file"""
	filename = 'updated_tables_response.txt'
	with open(filename, 'w') as f:
		f.write(response.text)
		f.close()

	""" Open file and read contents"""
	filename = 'updated_tables_response.txt'
	with open(filename, 'r') as f:
		contents = f.read()
        
	""" Regex to find any https entries"""
	matches = re.findall('https?://[^\s]+/en', contents)
    
	""" Filter out duplicate entries"""
	matches_no_duplicates = [*set(matches)]
    
	""" Retrieve links to .json files"""
	json_urls = [str(match) for match in matches_no_duplicates if '/JSON-stat/1.0' in match]
    
	""" Retrieve matrix codes"""
	new_list = [s.split('/')[-4] for s in json_urls]

	""" Get label and update date from .json"""
	labels=[]
	updated=[]

	for i in range(0, len(json_urls)):
		df_identity = pd.read_json(json_urls[i])
		labels.append(df_identity['dataset'].label)
		updated.append(df_identity['dataset'].updated)
		df_identity = df_identity.iloc[0:0]
    
	# Make a dataframe with all the info
	data_sets_list = pd.DataFrame({'Latest Update' : updated,
		'Identifier' : new_list,
		'Description' : labels,
		'JSON' : json_urls},
		columns=['Latest Update', 'Identifier','Description', 'JSON'])
	f.close()
	print(data_sets_list.loc[:, 'Latest Update':'Description'].to_string())
	return json_urls, data_sets_list

def user_index_entry(json_urls_list, retrieved_dataframe):
	'''user input for the address with validation'''
	while True:
		try:
			inp_number=int(input("\n Enter numeric index of dataset to retrieve .csv : "))
			if inp_number<=0:
				raise InvalidEntry
			elif inp_number>len(json_urls_list):
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid number: ")
		except ValueError:
			print("\n Please enter a valid number: ")
	identifier=retrieved_dataframe['Identifier'].iloc[inp_number]
	create_url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{0}/CSV/1.0/en'.format(identifier)
	with requests.Session() as s:
		request = s.get(create_url)
		returned = request.content
		decoded = returned.decode('utf-8')
		create = csv.reader(decoded.splitlines(), delimiter=',')
		my_list = list(create)
	df=pd.DataFrame(my_list)
	df.to_csv('{}.csv'.format(identifier), encoding='utf-8')
	print('Dataset preview: \n')
	print(df.head())
	return df

def main():
	welcome()
	generated=False
	
	while True:
		selection=menu()
		if (selection ==1) and (generated==False):
			json_urls, dataframe_list= recently_updated_datasets(user_input())
			dataframe=user_index_entry(json_urls,dataframe_list)
			generated=True
		elif (selection ==1) and (generated==True):
			dataframe=user_index_entry(json_urls,dataframe_list)
		else:
			quit()

if __name__=='__main__':
	main()
