import csv
import requests
import pandas as pd
import pathlib
import argparse
import sqlite3
import os


parser = argparse.ArgumentParser(description='Run ETL pipeline')
parser.add_argument('filepath', help = "This should be the desired filename if CSV/JSON or table name if SQL DB")
parser.add_argument('filetype', help = "Choose export method",choices=["json", "csv", "sql_db"])
parser.add_argument('--db_name',default="proj1.db", help = "Choose Database to connect to. If database name is not in current file, then new db will be created. Defaults to proj1.db")
args = parser.parse_args()

url = 'https://www.dnd5eapi.co/api/spells'

spell_list = requests.request("GET", url).json()


# This section borrowed and modified from Keefe
 
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

#adding a column
print("Adding Source Column\n")
spell_df["source"] = "SRD"

# Ask user export method
if args.filetype == "csv":
    spell_df.to_csv(args.filepath)
    print("CSV exported")
elif args.filetype == "json":
    spell_df.to_json(args.filepath)
    print("json exported")
elif args.filetype == "sql_db":
    print(args.db_name)
    if not os.path.exists(args.db_name):
        con = sqlite3.connect(args.db_name)
    else:
        con = sqlite3.connect(args.db_name)


    spell_df.to_sql(args.filepath, con)
    print("sql exported")
