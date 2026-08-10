# Creating dcitionaries
d = {"name":"mahesh","age":25,"school":"ZPHS"} #default declaration
d1={} #empty dictionary
d2=dict(name="mahesh",age=25,school="ZPHS") #constructor syntax
d3=dict([("name","Mahesh"),("age",25),("school","ZPHS")]) #from a list of tuples
print(d)
print(d1)
print(d2)
print(d3)

# Accesing values 
d={"Name":"Mahesh","Age":25,"school":"ZPHS"}
print(d["Name"]) #accesing value form Key
#print(d["salary"])  # it will throw errors because it didn't have slary key
#Fix
print(d.get("salary")) #Returns none if missing Key
print(d.get("Salary",-1)) #Returns -1 is missing Key
print(d.get("Age"))

#Adding element
d["college"]="Sri chaitanya junior college tirupati"
print(d.get("college"))

#Updating existing element in dictionary
d["Name"]="Jinka Mahesh reddy"
print(d.get("Name"))

# Removing Items from dictionary
del d["Age"]  # removes an element from dictionary but does not have capability to return removed element
print(d.get("Age",-1))
remoevd=d.pop("Name")       # Removes elemet and have capability to return removed element which can be used in future

#clearing
print(d)
d.clear()
print(d) #clears entire dictionary

#Checking if Key exists
d=dict(Name="JinkaMaheshReddy",Age=25,School="ZPHS")
print(d)
print("Name" in d)
print("Salary" in d)

#Iterating over dictionary elements
d=dict(a=1,b=2,c=3)
for i in d: # Here i is Key
    print(i) # printing the Keys
print("\n")

for i in d.keys(): #Explicit naming  of Keys but returns same as above
    print(i)
print("\n")

for i in d.values(): #Explicit naming of Values
    print(i) #returns Values
print()
for key,value in d.items():
    print(key,value) #returning both key and value
print()


#Dictionary comprehensions
d={x: x**2 for x in range(5)}
print(d)
# with condition
d={x: x**2 for x in range(10) if x%2==0}
print(d)
d={x: x**2 if x%2==0 else x for x in range(10)}
print(d)


# Nested dictionaries
Alphabets={"Vowels":{1:"a",2:"e",3:"i",4:"0",5:"u"},"Consonents":{1:"b",2:"c",3:"d",4:"f"}}
print(Alphabets["Vowels"][3])

# Merging
m1=dict(a=1,b=2,c=3)
m2=dict(d=4,e=5,f=6)
m3=m1|m2 
print(m1)
print(m2)
print(m3) # This merging creates new dictionary and will not modify original dictionaries
print()

m1=dict(a=1,b=2,c=3)
m2=dict(d=4,e=5,f=6)
m1.update(m2) # m1 dictionary will change in place and m2 will stay as original
print(m1)
print(m2)

#Dictionary keys must be hashable(Immutable)
d={(1,2):"coords1"} # correct tuple is immutable
 #d1={[1,2]:"coords2"} # incorrect list is mutable # throws error
print(d)

# Dictionary methods
print(len(m1))
print(list(m1.keys()))
print(list(m1.values()))
print(list(m1.items()))

#SetDefault
# If the given Key is present in dictionary it will return original value of that key without overriding
# If key is not present it will add the given key to dictionary
m1.setdefault("g",7)
print(m1)
m1.setdefault("g",986)  #will not override it present
print(m1)

# DefaultDict
# If we are adding value to a missing Key value it will throw error
# Default Dict Handles this by default without throwing error
from collections import defaultdict
d=defaultdict(int)
d["a"]+=1
d["a"]+=1
d["a"]+=2
d["c"]+=67
d["b"]+=3
print(d)