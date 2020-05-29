# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:37:22 2020

@author: Brodie
"""

import os


# Module for reading CSV files
import csv

count = 0
candidates = []
indexer = []
indexed = []
final = []
# csvpath = os.path.join('..', 'Poll','Resources', 'election_data.csv')
csvpath = os.path.join('..', 'Poll','Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # sum_row = 0
    # last_row = 0
    # max_row =0
    # min_row =0
    # change=[]
    counter =0
    index=0
    for row in csvreader:
        counter = counter +1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = index +1
            indexer.append(index)
            indexed.append(index)
with open(csvpath) as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    for row in csvreader:
        # print(row)          
        for x in candidates:
            if row[2] == x:
              indexer[candidates.index(x)]=indexer[candidates.index(x)]+1
                
            
# print(counter)
# print(candidates)
# print(indexer)
txtpath = os.path.join('..', 'Poll','analysis', 'output.txt')
file1 = open(txtpath,"w")#write mode               
print("Election Results")
file1.write("Election Results \n\n")
file1.write("Total Votes: ")
file1.write(str(counter))
file1.write("\n\n")

print("Total Votes: ", counter)

for a in range(len(candidates)):
    
    file1.write(candidates[a])
    file1.write("  ")
    file1.write(str(round(((indexer[a]-indexed[a])/counter)*100,2)))
    file1.write("%  ")
    file1.write(str(indexer[a]-indexed[a]))
    file1.write("\n")
    print(candidates[a], round(((indexer[a]-indexed[a])/counter)*100,2),"%",  indexer[a]-indexed[a])
    final.append(indexer[a]-indexed[a])
    # print(indexer[a]-indexed[a])
final2 = max(final)
# print(final2)

for a in range(len(candidates)):
    if final[a] == final2:
        print("Winner:", candidates[a])
        file1.write("\n Winner:")
        file1.write(candidates[a])

      

