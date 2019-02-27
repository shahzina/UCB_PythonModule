
import os
import csv

csvpath = os.path.join('..','Documents','Netflix_Ratings.csv')

video = input("What do you want to watch?")

found = False

with open(csvpath, newline ='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	#print(csvreader)
	for row in csvreader:
		if row[0] == video:
			print(row[0] + " is rated " + " with a rating of ")

			found = True 

			break 

	if found is False:
		print("We don't seem to have what you want.")

'''
setting a boolean is important.


'''