# Enumerate()
#Enumerate will help returning the items with proper index
names=["Jinka","Mahesh","Reddy"]
for i,j in enumerate(names):
    print(i,j)

# Zip()
#If 2 or more data types running together we use zip() instead of running 2 or more loops loops 
a=[4,5,6]
b=["Jinka","Mahesh","Reddy"]
for i in zip(a,b):
    print(i)

keys=[1,2,3]
values=["Jinka","Mahesh","Reddy"]
result=dict(zip(keys,values)) # 1st it will zip in tuples and converts to dictionary
print(result)

#transpose
matrix=[[1,2,3],[4,5,6],[7,8,9]]
result=list(zip(*matrix))
print(result)

#zip_longest
from itertools import zip_longest
a=[1,2,3]
b=["Jinka","Mahesh"]
for i in zip_longest(a,b,fillvalue="NA"): #for unequal length elements it will print NA
    print(i)
print(zip_longest(a,b)) #without converting to list it will return iterable object
print(list(zip_longest(a,b))) 

a=[1,2,3]
print(enumerate(a))
print(list(enumerate(a)))