"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

#import libraries
import numpy as np
#make list of input numbers
x=[int(i) for i in input("input>>").split()]
#create 1d array
a=np.array(x)
#reshape into 3D arrary and print output
print("output:\n",a.reshape(3,3))
