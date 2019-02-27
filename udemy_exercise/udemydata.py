'''
Title, Price, Subscriber Count, Number of Reviews, 
and Course Length into Python Lists.
'''
import os
import csv

input = os.path.join('..','Documents','web_starter.csv')

title = []
price =[]
subscriber_count = []
num_of_reviews = []
course_length =[]


with open(input, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	for row in csvreader:
		title.append(row[1])	
		price.append(row[4])
		subscriber_count.append(row[5])
		num_of_reviews.append(row[6])
		course_length.append(row[9])

clubbing = zip(title, price, subscriber_count, num_of_reviews,course_length)

output = os.path.join('..','Documents','web_starter_out.csv')

with open(output, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count","Number of Reviews","Course Length"])

    writer.writerows(clubbing)



