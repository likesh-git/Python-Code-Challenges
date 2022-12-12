"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
#With NumPy
​
#import libraries
import numpy as np
#create a random array of 40 integers from 5 - 15 using NumPy 
x = np.random.randint(5, 15, 40)
print("array:{}".format(x))
print("\nmost frequent value in array:{}".format(np.bincount(x).argmax()))
​
​
​
​
#Without NumPy using Counter class
​
#import libraries
import random
from collections import Counter
#create a random array of 40 integers from 5 - 15 using NumPy 
list1 =[random.randint(5 , 15) for i in range(0,40)]
#create a collection of counter based on the count of the numbers
dict1 = Counter(list1)
print("array:{}".format(list1))
#create a list which is sorted based on the count of the numbers and print
print("\nmost frequent value in array:{}".format(dict1.most_common()[0][0]))
​
