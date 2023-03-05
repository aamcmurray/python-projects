import requests
import json
import csv
import pandas as pd

def show_contents():
    index=[[0,'VSBA01', 'Births Registered'],
           [1,'VSDA02', 'Place of Death by Usual Residence'],
           [2,'VSDA01', 'Deaths Registered'],
           [3,'ABIRU', 'Annual Business Inquiry Reporting Unit Results'],
          [4, 'BUSINESSLGDBIG', 'Number of Businesses']]
    contents = pd.DataFrame(index, columns = ['Index','Code', 'Description'])
    print(contents)
    
def make_choice():
    choice= int(input("Enter index of selection: "))
    code=contents['Code'][choice]
    create_url='https://ws-data.nisra.gov.uk/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{0}/CSV/1.0/en'.format(code)
    return create_url

def api_get(input_url):
    with requests.Session() as s:
        request = s.get(input_url)
        returned = request.content
        decoded = returned.decode('utf-8')
        create = csv.reader(decoded.splitlines(), delimiter=',')
        my_list = list(create)
    df=pd.DataFrame(my_list)
    return df

def retrieve_data():
    df=api_get(make_choice())
    return df

if __name__ == "__main__":
  show_contents()
  retrieve_data()
