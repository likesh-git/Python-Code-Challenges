"""
Code Challenge
Name:
Baltimore City Analysis
Filename:
baltimore.py
Problem Statement:
Read the Baltimore_City_Employee_Salaries_FY2014.csv file
and perform the following task :

0. remove the dollar signs in the AnnualSalary field and assign it as a float
0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
Sort the data and display to show who get the highest salary
0. Try to group on JobTitle only and sort the data and display
0. How many employess are there for each JobRoles and Graph it
0. Graph and show which Job Title spends the most
0. List All the Agency ID and Agency Name
0. Find all the missing Gross data in the dataset


"""
import pandas as pd

import numpy as np

df = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv',header=0)


df['AnnualSalary'] = df['AnnualSalary'].astype(str)

df['AnnualSalary'].apply(lambda x: x.replace('$',''))

df['AnnualSalary'] = df['AnnualSalary'].astype(float)



# group the data
grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])


output = df.sort_values(['AnnualSalary'],ascending=0)
print (str(output.iloc[0,0])+" get the highest salary")


grouped = df.groupby(['JobTitle'])
sorted(grouped.keys())

# Top 10 jobroles according to employees numbers
df['JobTitle'].value_counts()[0:10].plot('bar')

#  which Job Title spends the most
aggregated.sort_values(['sum'],ascending=0,inplace=True)
print (str(aggregated.index[0])+" job title spends the most")

aggregated['sum'][0:10].plot('bar')

# List All the Agency ID and Agency Name
agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)

# Find all the missing Gross data in the dataset
df['GrossPay'].isnull().sum()