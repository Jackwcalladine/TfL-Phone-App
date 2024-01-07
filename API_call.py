import requests
import pandas as pd
import openpyxl 
import re

# Define a function to take in TfL API calls and return a dataframe from the JSON
def call_to_df(call):

    api_url = call
    response = requests.get(api_url)
    json_call = response.json()
    df = pd.DataFrame.from_dict(pd.json_normalize(json_call), orient='columns')

    return df

# Get all modes of transport, here we see that the overground line is called..."overground"
#print(call_to_df("https://api.tfl.gov.uk/Line/Meta/Modes"))

#api_url = "https://api.tfl.gov.uk/StopPoint/Mode/overground"
#response = requests.get(api_url)

# look at keys of the response, the stopPoints key points to a list of dictionaries, we can use the first entry
# to get the stationIDs
#response.json().keys()
#response.json()['stopPoints'][1].keys()
#response.json()['stopPoints'][1]['naptanId']

#counter = 0
#stationList = list()
#for i in response.json()['stopPoints']:
#    statresponse = response.json()['stopPoints'][counter]['naptanId']
#    stationList.append(statresponse)
#    counter += 1

# save the station list so we dont need to call it again
#stationListDF = pd.DataFrame(stationList)
#stationListDF.to_excel('stationList.xlsx', sheet_name='stations', index=False)

#r = re.compile(".*HACKNYW")
#filteredList = list(filter(r.match, stationList)) # Read Note below
#print(filteredList)

# Stoppoints, after looking through these we can see the first has all the arrivals
DF_910GHACKNYW = call_to_df("https://api.tfl.gov.uk/StopPoint/910GHACKNYW/Arrivals")
#DF_9100HACKNYW0 = call_to_df("https://api.tfl.gov.uk/StopPoint/9100HACKNYW0/Arrivals")
#DF_9100HACKNYW1 = call_to_df("https://api.tfl.gov.uk/StopPoint/9100HACKNYW1/Arrivals")
#DF_4900HACKNYW0 = call_to_df("https://api.tfl.gov.uk/StopPoint/4900HACKNYW0/Arrivals")
#DF_4900HACKNYW1 = call_to_df("https://api.tfl.gov.uk/StopPoint/4900HACKNYW1/Arrivals")

df_hackney = DF_910GHACKNYW
df_hackneyFiltered = df_hackney[['platformName', 'destinationName', 'timeToStation']]

df_hackneyFiltered['timeToStation'] = pd.to_numeric(df_hackneyFiltered['timeToStation'])
df_hackneyFiltered['timeToStation'] = df_hackneyFiltered['timeToStation'] / 60
print(df_hackneyFiltered)




