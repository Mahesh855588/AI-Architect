# sort()
#mutates in place
l=[1,2,3,4,5,9,8,7,6,5,4]
l.sort() # does not create new list,original will be changed
print(l)
l.sort(reverse=True)
print(l)

#Sorted()
#Creates new item ,does not change original list
# with key argument we can sort by condition
words = ["banana", "kiwi", "fig", "apple"]

print(sorted(words))               # ['apple', 'banana', 'fig', 'kiwi'] — default alphabetical
print(sorted(words, key=len))         # ['fig', 'kiwi', 'apple', 'banana'] — sorted by LENGTH instead

#operator.itemgetter
from operator import itemgetter
di=[("a",2),("b",4),("c",7)]
result=sorted(di,key=itemgetter(1))  #same functionality as lambda function
print(result)
# attrgetter
#sorting by attributes
from operator import attrgetter
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
people=[Person("Mahesh",25),Person("Jinka",36)]
result=sorted(people,key=attrgetter("age"))
print([i.name for i in result] )