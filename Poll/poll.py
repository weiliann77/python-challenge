# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:42:55 2020

@author: Brodie
"""


# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:00:00 2020

@author: Brodie
"""
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# import statistics
import pandas as pd
# Module for reading CSV files
# import csv

csvpath = os.path.join('..', 'Poll','Resources', 'election_data.csv')
df= pd.read_csv(csvpath, encoding="ISO-8859-1")
# data1 = df.head()
# print(data1)
# print(df.head())
# print(df.sum())
df1 = df.groupby("Candidate")
df6 = df1["Voter ID"].count().rename_axis('Candidate').reset_index(name='Votes')
df2 = df1["Voter ID"].count()
df3 = len(df)
# print(df2)
print('Total Votes:', df3)
df4 = pd.DataFrame((df2/df3))
df5 = df4.rename(columns={'Voter ID':'Votes'})
df7 = df5.merge(df6, on="Candidate")
df8 = df7.rename(columns={'Votes_x':'Vote Percentage','Votes_y':'Votes'})
print(df8)
# print(df8['Votes'].max())
val = df8['Votes'].max()
print("winner: " , df8.loc[df8['Votes']==val,'Candidate'].item())

txtpath = os.path.join('..', 'Poll','analysis', 'output.txt')
file1 = open(txtpath,"w")#write mode 
file1.write("Election Resuslts \n \n")
file1.write('total votes ')
file1.write(str(df3))
file1.write('\n')
file1.write('\n')
file1.write(str(df8))
file1.write('\n')
file1.write('\n')
file1.write("winner:  ")
file1.write(df8.loc[df8['Votes']==val,'Candidate'].item())
file1.close() 
# print(df3.dtypes)
# print(df2['Votes'].dtypes)


# print(df2.iloc[0:0,0:0])

# print(df1.sum())

# Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

#     # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

#     # # Read each row of data after the header
#     # sum_row = 0
#     # last_row = 0
#     # max_row =0
#     # min_row =0
#     # change=[]
#     # counter =0
    
#     for row in csvreader:
#     #     sum_row = int(row[1])+sum_row
#     #     if (int(row[1])-last_row) > max_row:
#     #         max_row=int(row[1])-last_row
#     #     if (int(row[1])-last_row) < min_row:
#     #         min_row=int(row[1])-last_row
#     #     if counter != 0:
#     #         change.append((int(row[1])-last_row))
#     #     counter = counter +1
#     #     last_row = int(row[1])
#         print(row)
#     # x = statistics.mean(change)
#     # print(sum_row)
#     # print(max_row)
#     # print(min_row)
#     # # print(x)
#     # print(counter)