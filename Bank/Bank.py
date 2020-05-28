# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:00:00 2020

@author: Brodie
"""
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import statistics

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Bank','Resources', 'budget_data.csv')

# Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    sum_row = 0
    last_row = 0
    max_row =0
    min_row =0
    change=[]
    counter =0
    
    for row in csvreader:
        sum_row = int(row[1])+sum_row
        if (int(row[1])-last_row) > max_row:
            max_row=int(row[1])-last_row
            max_row_date = row[0]
        if (int(row[1])-last_row) < min_row:
            min_row=int(row[1])-last_row
            min_row_date = row[0]
        if counter != 0:
            change.append((int(row[1])-last_row))
        counter = counter +1
        last_row = int(row[1])
        # print(row)
    x = statistics.mean(change)

    print("Total Months:", counter)
    print("Total: $:", sum_row)
    print('Average Change: $', round(x,2))
    print("Greatest Increase in Profits:", max_row_date, " $", max_row)
    print("Greatest Decrease in Profits:", min_row_date, " $", min_row)
    line1 = ("Total Months:", counter)
    line2 = ("Total: $:", sum_row)
    line3 = ('Average Change: $', round(x,2))
    line4=("Greatest Increase in Profits:", max_row_date, " $", max_row)
    line5=("Greatest Decrease in Profits:", min_row_date, " $", min_row)

    line1="Total Months:", counter
    txtpath = os.path.join('..', 'Bank','analysis', 'output.txt')
    file1 = open(txtpath,"w")#write mode 
    file1.write("Financial Analsyis \n")
    file1.write("Total Months:") 
    file1.write(str(counter))
    file1.write('\n')
    file1.write("Total: $:") 
    file1.write(str(sum_row))
    file1.write('\n')
    file1.write('Average Change: $')
    file1.write(str(round(x,2)))
    file1.write('\n')
    file1.write("Greatest Increase in Profits: ") 
    file1.write(str(max_row_date))
    file1.write(" $") 
    file1.write(str(max_row))
    file1.write('\n')
    file1.write("Greatest Decrease in Profits: ") 
    file1.write(str(min_row_date))
    file1.write(" $") 
    file1.write(str(min_row))
     

    # file1.write("Tomorrow \n") 
    # file1.write("Total Months:", counter)
    # file1.write("Total: $:", sum_row)
    # file1.write('Average Change: $', round(x,2))
    # file1.write("Greatest Increase in Profits:", max_row_date, " $", max_row)
    # file1.write("Greatest Decrease in Profits:", min_row_date, " $", min_row)
    
    file1.close() 
    # print(min_row)
    # print(x)
    # print(counter)
    # print(max_row_date)