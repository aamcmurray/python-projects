def updated_datasets():
    # This function is designed to search for updates since a given date and return the links of relevant .csv datasets
    csv_urls=[]
    
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
    
    # Retrieve links to .csv files
    csv_urls = [match for match in matches_no_duplicates if '/CSV/' in match]
    
    f.close()
    print(csv_urls)
    return csv_urls
