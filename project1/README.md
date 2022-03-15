# Project 1 ETL data processor 
While looking for D&D related data sources, I stumbled upon Dan Keefe's project analyzing monsters in D&D (https://peritract.github.io/2020/05/14/dungeons-and-data/.) This project used the Dungeons and Dragons API. While his project was about analyzing monsters, I have made my project about the spells available in the game, as managing spell information can be difficult sometimes.


## Usage

Running `python3 etl.py -h` will give the following output:

```
usage: etl.py [-h] [--db_name DB_NAME] filepath {json,csv,sql_db}

Run ETL pipeline

positional arguments:
  filepath           This should be the desired filename if CSV/JSON or table name if SQL DB
  {json,csv,sql_db}  Choose export method

optional arguments:
  -h, --help         show this help message and exit
  --db_name DB_NAME  Choose Database to connect to. If database name is not in current file, then new db will be created. Defaults to proj1.db
```

As an example, if you would like to take the spell data and export it as a csv file names `test.csv`, you would run `python3 etl.py test.csv csv`. 

If you wanted to export to a database named `test.db` with a table named `spells`, run `python3 etl.py spells sql_db --db_name test.db`



## Project Requirements
For the project, I need to:

- [x] Fetch / download / retrieve a remote data file by URL, or ingest a local file mounted.
    * For this project, I used the D&D Api to obtain the data set. This code is modified from Keefe's implementation of pulling the data


- [x] Convert the general format and data structure of the data source from JSON to CSV, from CSV to JSON, from JSON into a SQL database table, etc. There must be the option to convert any source to any target. So, if CSV is an input, I want the user to choose an output EXTRA – Use and API (like twitter) to pull information realtime.
    * This code will pull the data directly from the API, and convert to the filetype requested by the user, depending on how the command is run. For more informataion, run `python3 etl.py -h`


- [x] Modify the number of columns from the source to the destination, reducing or adding columns. 
    * Added a column to indicate the source of the information for the API is from the SRD Ruleset (https://dnd.wizards.com/articles/features/systems-reference-document-srd). This is a useful column to have in the event a user may want to combine this information with spells from other sources (Player's Handbook, Tasha's Cauldron of Everything, Homebrew content, etc.)


- [x] The converted (new) file should be written to disk (local file) or written to a SQL database. 
    * This is tied to the 2nd requirement
    - [x] CSV
    - [x] JSON
    - [x] SQL DB (currently converting all objects into strings)


- [x] Generate a brief summary of the data file ingestion including Number of records and Number of columns 
    * Simple print statement is made. As of current build, output should be `There are 319 records and 21 columns`

- [x] Error handling
    * Some of it is done with the Arg Parse to help make sure enough information is there
    * Try catch added when writing the files -- if the filepath tries to write to a non-existant file, the error is caught.
    * Provided a warning when the filename doesn't match.

## Other features that would be cool

- [ ] Fix the wierdness with having an extra flag for the db_name. It's really wierd. I don't know why I did that. 

- [ ] I want to provide an easy way to add custom spells, as well as spells from other source books still need to think on how this feature would work. This is beyond the scope of the project though.

- [ ] Querying spells so that information could be obtained and turned into an easy cheat sheet would be super nice. 