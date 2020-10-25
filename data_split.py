import os, csv, sqlite
import csv_to_sqlite 

options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["my_data/distance_between_sector.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "sqlite/sectors_map.db", options)

