import json
import numpy as np 
import pandas as pd 

items = json.loads('[{"id":1,"text":"abc"}]')

for item in items:
    print(item['text']) 

myindex = ['USA','Canada',['Mexico']]
mydata = [1776,1867,1821]
myser = pd.Series(data=mydata, index=myindex)
print(myser)


ages = {'Sam':5,'Frank':10,'Spike':7}

q1 = {'Japan':80,'China':450,'India':200,'USA':250}
q2 = {'Brazil':100,'China':500,'India':210,'USA':260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

#broadcast operations 
#print(sales_q1.add(sales_q2, fill_value = 0))

df = pd.read_csv('/Users/andrewcarson/Udemy/UNZIP_ME_FOR_NOTEBOOKS/03-Pandas/tips.csv')
print(df)

"""
NumPy:
my_matrix =[[1,2,3],[4,5,6],[7,8,9]]
#makes two dimensional 
#print(np.array(my_matrix))
#2 is step size 
#print(np.arange(0,10,2))

#5 rows, 5 columns 
#print(np.zeros((5,5)))
#print(np.ones((5,5)))

#first argument start, 2nd stop, third: how many numbers evenly spaced between the first two 
#print(np.linspace(0,10,3))

#random distributions
#uniform distributioin means same likelihood of being picked 
#print(np.random.rand(5,2))
#standard normal distribution means likelihood is closre to 1, also mean of 0 means negatives can be returned 
#print(np.random.randn(5,2))
#print(np.random.randint(0,101,(4,5)))
#print(np.random.seed(42))
#print(np.random.rand(4))

#arr = np.arange(0,25)
#print(arr.reshape(5,5))
#randomIntegers = np.random.randint(0,101,10)
#print(randomIntegers)
#print(randomIntegers.max())
#print(randomIntegers.argmax()) #index location of highest value 
#print(randomIntegers.min())

arr = np.arange(0,11)
#select one 
print(arr[8])
#select slice starting at 0
#print(arr[0:5]) #or arr [:5] when wanting 0 or [5:] when wanting to go from 5 to end 
"""