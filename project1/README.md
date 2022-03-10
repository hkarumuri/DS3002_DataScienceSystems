# Project 1 ETL data processor 
While looking for D&D related data sources, I stumbled upon Dan Keefe's project analyzing monsters in D&D (https://peritract.github.io/2020/05/14/dungeons-and-data/.) This project used the Dungeons and Dragons API. While his project was about analyzing monsters, I have made my project about the spells available in the game, as managing spell information can be difficult sometimes.

For the project, I need to:

- [x] Fetch / download / retrieve a remote data file by URL, or ingest a local file mounted.
    * For this project, I used the D&D Api to obtain the data set. This code is modified from Keefe's implementation of pulling the data


- [ ] Convert the general format and data structure of the data source from JSON to CSV, from CSV to JSON, from JSON into a SQL database table, etc. There must be the option to convert any source to any target. So, if CSV is an input, I want the user to choose an output EXTRA – Use and API (like twitter) to pull information realtime.
    * The framework to allow this choice is currently implemented, but actually writing to the various options has not been coded yet
    * I want to change this to default printing the table, and then passing in the data type through a command line variable? I like the idea of this being more like a CLI tool, but this is a stretch goal.


- [x] Modify the number of columns from the source to the destination, reducing or adding columns. 
    * Added a column to indicate the source of the information for the API is from the SRD Ruleset (https://dnd.wizards.com/articles/features/systems-reference-document-srd). This is a useful column to have in the event a user may want to combine this information with spells from other sources (Player's Handbook, Tasha's Cauldron of Everything, Homebrew content, etc.)
    - [ ] I want to provide an easy way to add custom spells, still need to think on how this feature would world


- [ ] The converted (new) file should be written to disk (local file) or written to a SQL database. 
    * This is tied to the 2nd requirement


- [x] Generate a brief summary of the data file ingestion including Number of records and Number of columns 
    * Simple print statement is made. As of current build, output should be `There are 319 records and 21 columns`




