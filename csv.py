import pandas as pd
import random
import csv
import argparse

parser = argparse.ArgumentParser(  #Parse command line arguments 
	description="Specify the number of entries you want to return"
)
parser.add_argument('-w', '--winners', default=1, type=int)
arguments = parser.parse_args()

with open('*.csv', 'r') as infile: # remove duplicate entries from the original CSV and output to a new CSV
	data = pd.read_csv(infile)
	data.sort_values(["Customer Name","Email"], inplace=True)
	clean_data = data.drop_duplicates(inplace=False)
	clean_data.to_csv('decwin.csv')

with open ('*.csv', 'r') as outfile: #open new CSV file 

	words = outfile.readlines()
	
	for _ in range(arguments.winners): 
		print(random.choice(words)) # Print winning names
