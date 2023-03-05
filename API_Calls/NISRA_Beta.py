import requests
import json
import csv
import pandas as pd
import re

def updated_datasets():
    # Search for updates since a given date and return the links of relevant .csv datasets, filters duplicate entries
    # outputs a JSON with the response to the request and a dataframe with all available data sets 
    
    year= input("Enter Year (YYYY): ")
    month= input("Enter Month (MM): ")
    day= input("Enter Date (DD): ")
    date=str(year)+'-'+str(month)+'-'+str(day)
    
    # Make request
    url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadCollection/{}/en'.format(date)
    response = requests.get(url)

    # Write response text to a JSON file
    filename = 'updated_tables_response.txt'
    with open(filename, 'w') as f:
        f.write(response.text)
        f.close()

    # Open file and read contents
    filename = 'updated_tables_response.txt'
    with open(filename, 'r') as f:
        contents = f.read()
        
    # Regex to find any https entries
    matches = re.findall('https?://[^\s]+/en', contents)
    
    # Filter out duplicate entries
    matches_no_duplicates = [*set(matches)]
    
    # Retrieve links to .json files
    json_urls = [str(match) for match in matches_no_duplicates if '/JSON-stat/1.0' in match]

    for i in range(len(json_urls)):
        print(json_urls[i])
    # Retrieve matrix codes
    new_list = [s.split('/')[-4] for s in json_urls]

    # Get label and update date from .json
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
        
    return data_sets_list

def select_data_set():
    # Takes user input to create the .csv path
    user_choice=int(input("Enter index of selection: "))
    identifier=data_sets_list['Identifier'].iloc[user_choice]
    create_url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{0}/CSV/1.0/en'.format(identifier)
    return create_url

def csv_get(input_url):
    # Retrieves the .csv if it exists and outputs a dataframe
    with requests.Session() as s:
        request = s.get(input_url)
        returned = request.content
        decoded = returned.decode('utf-8')
        create = csv.reader(decoded.splitlines(), delimiter=',')
        my_list = list(create)
    df=pd.DataFrame(my_list)
    return df

if __name__ == "__main__":
    data_sets_list=updated_datasets()
    data_sets_list
    csv_get(select_data_set())
