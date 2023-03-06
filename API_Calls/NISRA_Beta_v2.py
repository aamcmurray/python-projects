# Libraries
import requests
import json
import csv
import pandas as pd
import re
from datetime import datetime
from tabulate import tabulate
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

def request_contents():
	""" Request"""
	url = 'https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadCollection/2000-01-01/en'
	response = requests.get(url)
	return response

def encode_response(url_response):
	""" .json file creation and utf-8 encoding"""
	filename = 'available_datasets.json'
	with open(filename, 'wb') as f: 
		f.write(url_response.content)
		f.close()
	with open(filename, encoding='utf-8') as f:  
		data = json.load(f)
	f.close()
	return data

def build_dataframe(returned_data):
	""" Builds a pandas dataframe by combing through the .json tags for information on the datasets and where to obtain them.""" 
	df = pd.DataFrame(columns=['Code','Label','Sources', 'Updated'])
	for j in range(0, len(returned_data['link']['item'])):
		code = returned_data['link']['item'][j]['extension']['matrix']
		label = returned_data['link']['item'][j]['label']
		#json = returned_data['link']['item'][j]['href']
		#csv = returned_data['link']['item'][j]['link']['alternate'][0]['href']
		updated = returned_data['link']['item'][j]['updated']
		sources = [returned_data['link']['item'][j]['link']['alternate'][i]['href'] for i in range(len(returned_data['link']['item'][j]['link']['alternate']))]
		"""new_row = {'Code': code,
									'Label': label,
								#	'JSON': json,
								#	'CSV': csv,
									'Sources': sources,
									'Updated': updated}"""
		df = pd.concat([df, pd.DataFrame.from_records([{'Code': code,
			'Label': label,
		#	'JSON': json,
		#	'CSV': csv,
			'Sources': sources,
			'Updated': updated}])], ignore_index=True)
		#df = df.append(new_row, ignore_index=True)
	""" Builds an additional condensed dataframe to show the contents."""
	condensed_df=df[['Code','Label','Updated']]
	return df, condensed_df

def show_dataframe(df):
	""" Make the output easier to read"""
	print(df.to_markdown())

def additional_information(mat_code):
	"""Additional information relating to a specific dataset can be requested through this function."""
	response = requests.get('https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{}/JSON-stat/2.0/en'.format(mat_code))
	filename = '{}.json'.format(mat_code)
	file_data=response.json()
	contact_name=file_data['extension']['contact']['name']
	contact_email=file_data['extension']['contact']['email']
	contact_phone=file_data['extension']['contact']['phone']
	subject_value=file_data['extension']['subject']['value']
	product_code=file_data['extension']['product']['code']
	product_value=file_data['extension']['product']['value']
	additional_info_df=pd.DataFrame(columns=['Subject Value','Product Code', 'Product Value', 'Contact','Email','Phone'])
	"""new_row = {'Subject Value':subject_value,
					'Product Code':product_code, 
					'Product Value':product_value, 
					'Contact':contact_name,
					'Email':contact_email,
					'Phone':contact_phone}"""
	additional_info_df = pd.concat([additional_info_df, pd.DataFrame.from_records([{'Subject Value':subject_value,
		'Product Code':product_code, 
		'Product Value':product_value, 
		'Contact':contact_name,
		'Email':contact_email,
		'Phone':contact_phone}])], ignore_index=True)
	#additional_info_df = additional_info_df.append(new_row, ignore_index=True)
	return additional_info_df

def welcome():
	print("_______________________")
	print("A Py I...............v2")
	print("_______________________ \n")
	print("This tool is designed to search and retrieve datasets available at: https://data.nisra.gov.uk/")
	print("Please use responsibly, as a general rule, more than 30 API calls in a minute is too many.")
	print("Excessive requests can lead to HTTP error 429 - too many requests. \n")

def menu():
	print("_______________________")
	print("MENU")
	print("_______________________ \n")
	print("1. Retrieve list of datasets.")
	print("2. Find out more about a dataset.")
	print("3. Download a dataset (.csv).")
	print("4. Quit.\n")
	'''user input for menu selection with validation'''
	while True:
		try:
			menu_num=int(input("\n Enter choice: "))
			if menu_num<=0:
				raise InvalidEntry
			elif menu_num>4:
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid number: ")
		except ValueError:
			print("\n Please enter a valid number: ")
	return menu_num

#df, condensed_df=build_dataframe(encode_response(request_contents()))
#show_dataframe(condensed_df)
#show_dataframe(df)
def download_dataset(retrieved_dataframe):
	'''user input for the address with validation'''
	while True:
		try:
			inp_number=int(input("\n Enter numeric index of dataset to retrieve .csv : "))
			if inp_number<=0:
				raise InvalidEntry
			elif inp_number>len(retrieved_dataframe):
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid number: ")
		except ValueError:
			print("\n Please enter a valid number: ")
	identifier=retrieved_dataframe['Code'].iloc[inp_number]
	create_url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{0}/CSV/1.0/en'.format(identifier)
	with requests.Session() as s:
		request = s.get(create_url)
		returned = request.content
		decoded = returned.decode('utf-8')
		create = csv.reader(decoded.splitlines(), delimiter=',')
		my_list = list(create)
	df_preview=pd.DataFrame(my_list)
	df_preview.to_csv('{}.csv'.format(identifier), encoding='utf-8')
	print('Dataset preview: \n')
	print(df_preview.head())
	return 

def which_dataset(retrieved_dataframe):
	'''user input for the address with validation'''
	while True:
		try:
			inp_number=int(input("\n Enter numeric index of dataset to retrieve additional information: "))
			if inp_number<=0:
				raise InvalidEntry
			elif inp_number>len(retrieved_dataframe):
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid number: ")
		except ValueError:
			print("\n Please enter a valid number: ")
	identifier=retrieved_dataframe['Code'].iloc[inp_number]
	return str(identifier)

def main():
	welcome()
	data_frame_generated=False
	while True:
		menu_selection=menu()
		""" Generate a dataframe and print it to screen."""
		if ((menu_selection==1) and (data_frame_generated==False)):
			df, condensed_df=build_dataframe(encode_response(request_contents()))
			show_dataframe(condensed_df)
			data_frame_generated=True
			""" Print dataframe to screen."""
		elif ((menu_selection==1) and (data_frame_generated==True)):
			show_dataframe(condensed_df)
			data_frame_generated=True
			""" Generate a data frame and print dataframe to screen. Retrieve additional information on a specified dataset."""
		elif ((menu_selection==2) and (data_frame_generated==False)):
			df, condensed_df=build_dataframe(encode_response(request_contents()))
			show_dataframe(condensed_df)
			code_out=which_dataset(df)
			additional_info_df=additional_information(code_out) # < - need to write this function
			show_dataframe(additional_info_df)
			data_frame_generated=True
			""" Retrieve additional information on a specified dataset."""
		elif ((menu_selection==2) and (data_frame_generated==True)):
			code_out=which_dataset(df)
			additional_info_df=additional_information(code_out) # < - need to write this function
			show_dataframe(additional_info_df)
			data_frame_generated=True
			""" Generate a data frame and print dataframe to screen. Download a specified dataset."""
		elif ((menu_selection==3) and (data_frame_generated==False)):
			df, condensed_df=build_dataframe(encode_response(request_contents()))
			show_dataframe(condensed_df)
			download_dataset(df)
			data_frame_generated=True
			""" Generate a data frame and print dataframe to screen. Download a specified dataset."""
		elif ((menu_selection==3) and (data_frame_generated==True)):
			download_dataset(df)
			data_frame_generated=True
		else:
			quit()

if __name__=='__main__':
	main()
