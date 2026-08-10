# Creating sets
# in sets duplicate elements will be collapsed
s={1,2,3,4,5} # default set creation
s1=set() #empty set
s2=set([1,2,3,4,5,5,4,3,2,1])
print(s)
print(s1)
print(s2)

# Adding elements to set
s.add(9)
print(s)

# Removing elements
s.remove(2) #It will remove element ,raises error if element is not present
print(s)
#Correct way
s.discard(3)
s.discard(18) # it will not throw error even if element is missing
print(s)

popped=s.pop() #removes arbitrary(1st) and returns removed elements
print(s)


# Sets Core operations
a={1,2,3,4}
b={3,4,5,6}
print(a|b)  #Union
print(a.union(b))
print(a&b)  #intersection
print(a.intersection(b))
print(a-b)  #elements in a but not b
print(a.difference(b))
print(b-a) #elements in b but not in a
print(b.difference(a))
print(a^b) #symmetric difference (in either but not both)
print(a.symmetric_difference(b)) 

# Relation between sets
a={1,2}
b={1,2,3,4}
print(a.issubset(b)) # every element of a present in b
print(b.issuperset(a)) # all a present in b
print(a.isdisjoint({1,2})) # no common element in both sets
print(a.isdisjoint({6,9}))
print(a.isdisjoint(b))

# Set comprehension
square={i**2 for i in range(10)}
print(square) # sets are unorders based on hashtable it will place elements in sets
print(sorted(square))

# Sets require hashable elements
# s={1,2,3,4,[1,23]} #throws error because list is not hashable

# Frozen set
# frozen set is immutable can contain mutable elements which cannot be changed after adding
f=frozenset([3,4,5])
print(f)