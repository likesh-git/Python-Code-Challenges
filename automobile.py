
"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
      4. Make a pie chart for all car makers
      
"""


import pandas as pd
import matplotlib.pyplot as plt


# Reading CSV file
df = pd.read_csv('Automobile.csv')


'''1. Handle the missing values for Price column'''
# Converting the datatype of price column from object to flaot
df["price"] = df["price"].astype(float)

# Filling the missing values with average of price column
df["price"] = df["price"].fillna(df["price"].mean())


'''2. Get the values from Price column into a numpy.ndarray'''
# Converting the price column into a numpy.ndarray
price_numpy_array = df["price"].values


'''3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price'''
print ( "Minimum Price is {0}".format( df["price"].min() ) )
print ( "Maximum Price is {0}".format( df["price"].max() ) )
print ( "Average Price is {0}".format( round( df["price"].mean(), 2 ) ) )
print ( "Standard Deviation of Price is {0}".format( round( df["price"].std(), 2 ) ) )


'''4. Make a pie chart for all car makers'''
# Make a pie chart for all car makers

series = df["make"].value_counts()

print (series.index[0:11])
print (series.values[0:11])

explode = (0.5,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


for x,y in zip(series.index, series.values):
    print (x,y)
