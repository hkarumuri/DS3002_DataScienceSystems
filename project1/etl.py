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

if args.filetype in set(['json', 'csv']):
    parsed_filepath = args.filepath.split(".")
    print(parsed_filepath)
    if args.filetype != parsed_filepath[-1]:
        print("WARNING: Inputted filetype and and filepath do not match. Using some of these files may not work.")
else:
    parsed_filepath = args.db_name.split(".")
    if "db" != parsed_filepath[-1]:
         print("WARNING: Inputted filetype and and filepath do not match. Using some of these files may not work.")

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
    try:
        spell_df.to_csv(args.filepath)
        print("CSV exported")
    except(OSError) as e:
        print("ERROR: ")
        print(e)

elif args.filetype == "json":
    try:
        spell_df.to_json(args.filepath)
        print("json exported")
    except(OSError) as e:
        print("ERROR: ")
        print(e)   

elif args.filetype == "sql_db":
    # convert objects to strings in data frame
    try:
        obj_cols = spell_df.select_dtypes(object).columns
        test = spell_df[obj_cols].astype("string")
        spell_df[obj_cols] = spell_df[obj_cols].astype("string")
        
        if not os.path.exists(args.db_name):
            con = sqlite3.connect(args.db_name)
        else:
            con = sqlite3.connect(args.db_name)
        spell_df.to_sql(args.filepath, con, if_exists="append")
        print("sql exported")
    except(OSError) as e:
        print("ERROR: ")
        print(e)


