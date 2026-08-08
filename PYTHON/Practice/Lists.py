l=[1,2,3,4,5,6,7]
l[1:3]=[]
print(l)

del l[0]
print(l)

l=[1,2,3,4,5,6,7,8]
print(min(l))
print(max(l))
print(sum(l))
print(len(l))

m=[[1,2,3],[4,5,6],[7,8,9]]
print(m[2][0])
print([[row[0] for row in m]])

l=[9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]
s=set(l) #removes duplicates amd makes set
l=list(s)  #makeing list from set
print(s)
print(l)
print(sorted(l)) #orders it

#indexing and slicing
l=[1,2,3,4,5,6,7,8,8,]
print(l[0])
print(l[5])
print(l[0:5])
print(l[:6])
print(l[7:])
print(l[::-1])
print(l[::3])

#Mutability
l=[1,2,3]
l[0]=100 # lists can be changed in place
print(l)

#methods
l=[1,2,3,54232,2,3,567,43,]
l.append(678)
print(l)
l.insert(1,876)
print(l)
l.remove(2) # removes 1st occurence of value 2
print(l)
l.pop() # removes  and returns last item
print(l)
l.pop(0) # removes and returns item at index 0
print(l)
l.sort() # sorts in place
print(l)
l.sort(reverse=True)#sorts in descending order
print(l)
l.reverse()
print(l)
l.count(1) # counts instances of 1
print(l)
l.index(4) # returns index of 1st occurence of 4
print(l)
l.extend([5,7,89,89,3,43,22,5,67,8,9]) # appends multiple iteams at once
print(l)
l.clear() # empties the list
print(l)


#sort()
l=[4,3,5,6,2,34,7]
l=l.sort()
print(l) #returns none after sorting the values will stay in same object in memory but we are accesing different l so it returns none
print(l.sort()) # same wrong implementations

#correct way need to access same object from memory
l=[43,2,2,6,78,2,3,8,9,3,3]
l.sort()
print(l) # accessing same object from memory

#sorted() # here it will create separate copy  without affecting original list
l=[65,32,7,32,8,3,0,6]
m=l.sorted() #now m will have different values
m.append(7)
print(l) # l will not be affected after appending to m

#List comprehensions
print([x**2 for x in range(10)]) # returns squares
print([x for x in range(10) if x%2==0])# evens
print([x for x in range(10) if x%2!=0])#odds
#transformation +condition
print([x**2 if x%2==0 else x for x in range(10)]) #if evens make squares else print odds

#nested list comprehensions
m=[[1,2,3],[4,5,6],[7,8,9]]
print([num for i in m for num in m])



#copying 

a=[1,2,3]
b=a # this is not a copy both a and b are labels of same objects in memory
b.append(8) 
print(a) # a will change

#shallow copy with no nested loops
a=[1,2,3,4]
b=a.copy() # now b is independent
b.append(8)
print(a) #a will not affect

#shallow copy with nested loops
a=[1,2,3,4,[1,2,3,4]]
b=a.copy()
b[4].append(78)# now a will also change because nested loops will be shared refernece
print(a) # nested list will change
c=a[:] # this is another way of shallow copy both are same

#deep copy
a=[1,2,3,[4,5,6]]
b=copy.deepcopy(a)
b[3].append(7) # now b is entirely independent 
print(a) # now a will not change




