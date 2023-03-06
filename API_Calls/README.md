# A. Py. I  v1

[NISRA_Beta.py](https://github.com/aamcmurray/python-projects/blob/master/API_Calls/NISRA_Beta.py) is a Python script that retrieves a list of data sets available at [NISRA](https://data.nisra.gov.uk/) It accepts user input. Select a dataset by index to download the dataset as a .csv to the current location. A preview of the data set will also be shown. This code uses regex to extract http values from the JSON files.

[NISRA_Beta_v2.py](https://github.com/aamcmurray/python-projects/blob/master/API_Calls/NISRA_Beta_v2.py) is a much cleaner, faster implimentation of the above code that works with the JSON files keys and values to find information. Has additional features such as the ability to get additional information relating to data sets (product codes and values along with contact information). 

[NISA_API_2.ipynb](https://github.com/aamcmurray/python-projects/blob/master/API_Calls/NISA_API_2.ipynb) shows some of the functions used in NISRA_Beta.py being applied in a Jupyter Notebook.

The programme is currently very simple however in future will enable selection of date ranges, filtering datasets, downloads by reference code and data will be sorted by category rather than date of the last update. 

This programme, or functions within it, should be useful to anybody who needs to access the same data sets repeatedly at defined time intervals (for instance to update dashboards or produce similar reports over time).
