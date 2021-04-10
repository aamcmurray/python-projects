from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt
import numpy as np


url='https://www.worldometers.info/coronavirus/country/uk/'
parsed_html=requests.get(url)
soup=BeautifulSoup(parsed_html.content, 'html.parser')

scripts = soup.find_all('script')
script=str(scripts[21])

def get_dates():
	dates = script.split("categories: [",1)[1].split("]",1)[0]
	dates = "["+dates+"]"
	dates = json.loads(dates)
	return dates

def get_data():
	data = script.split("data: [",1)[1].split("]",1)[0]
	data = "["+data+"]"
	data = json.loads(data)
	return data

def m_y_convert(input_list):
	output=[]
	for i in range(0, len(input_list)):
		output.append(input_list[i][:3]+' '+input_list[i][8:])
	return output

def date_conversion(inputdates):
	new_dates=m_y_convert(inputdates)
	unique_indices=[]

	i=0
	unique_indices.append(0)
	while i < len(new_dates)-1:
		if new_dates[i+1]==new_dates[i]:
			i+=1
		else: 
			unique_indices.append(i+1)
			i+=1
	return new_dates,unique_indices

def main():
	dates=get_dates()
	data=get_data()
	new_dates,unique_indices=date_conversion(dates)
	plt.bar(new_dates,data,color='#314e52')
	ax = plt.gca()
	ax.ticklabel_format(useOffset=False, style='plain', axis='y')
	ax.set_facecolor('#e7e6e1')
	for tick in ax.get_xticklabels():
   		tick.set_rotation(45)
	plt.title('Total Covid Cases in the U.K.',fontsize=16)
	plt.xlabel('Date',fontsize=12)
	plt.ylabel('Total Covid Cases',fontsize=12)
	plt.text(-3.5,5000000, 'Data source: https://www.worldometers.info/coronavirus/country/uk/',fontsize=8)
	plt.draw()
	plt.show()

if __name__ == "__main__":
    main()
