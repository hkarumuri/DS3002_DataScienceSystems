import csv
import requests
import pandas as pd

url = 'https://www.dnd5eapi.co/api/spells'

spell_list = requests.request("GET", url).json()

#print(spell_list)

#Attempt at obtaining detailed spell information using Apply
#def spell_lookup(url_index):
#    base_url = 'https://www.dnd5eapi.co'
#    #return base_url + url_index
#    return requests.get(base_url + url_index).json

#print(df["url"].apply(spell_lookup))
# Holder for spell details

# pulling data using 
spell_details = []
# For each spell in the list,
for spell in spell_list["results"]:
    # Get the monster details
    url = f"http://www.dnd5eapi.co/api/spells/{spell['index']}"
    details = requests.get(url).json()
    # And add them to the holder
    spell_details.append(details)

spell_df = pd.DataFrame(spell_details)
data_info = spell_df.shape
print(f"There are {data_info[0]} records and {data_info[1]} columns\n")

print("Adding Source Column\n")
spell_df["source"] = "SRD"

# Ask user export method

options = set(['csv', 'json', 'sql'])
method = ""

while method not in options:
    method = input("How would you like to export? \n Options: \n\t * csv\n\t * json\n\t * sql\n\n")
    if(method not in options):
        print("Cannot export to that. please try a different option")

if method == "csv":
    print("CSV exported")
elif method == "json":
    print("json exported")
elif method == "sql":
    print("sql exported")
