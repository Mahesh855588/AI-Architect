# Variables
# variable is a name that refers to a value in memory
x=6
#6 is an integer object in memory and x will be the label of it

#Declaring variables
age=24
name="Jinka Mahesh"
height=5.8
is_learning=True
#python figures out the type automatically based on the value assigned

#Data types
age=25
print(type(age)) #class int

price= 60.6
print(type(price)) # class float

name="Jinka Mahesh"
print(type(name))  #class string

is_active=True
print(type(is_active)) #class bool

result=None
print(type(result))  #class NoneType


#Dynamic typing
x=5 #x is integer
x="hello" #now x is string
x=[1,2,3] # now x is list

#NamingRules
    #Must start with a letter or underscore (_), never a number
    #Can contain letters, numbers, underscores after that
    #Case-sensitive: age and Age are two different variables
valid_name="ok"
_private="ok"
#2ndPlace="error" can't start with number
#my-var="error"  hyphens are not allowed

#Multiple assignment
#assign different values in one line
x,y,z=1,2,3
x=y=z=0


#Checking variable type
x=5
print(type(x))
print(isinstance(x,int))


#type conversion
#string to number
a="14"
a=int(a)

#number to string
a=16
a=str(a)

#string to float
a="18"
a=float(a)

#string to int
a="19"
a=float(a) # step 1
a=int(a) #step 2


#Mutability

#int,float,string,bool,tuple are immutable
#once created their values cannot be changed -reassignment creates new object
x=5
y=x
y=10
print(x) # x is 5 (immutable)

#list,dict,sets are mutable
#their contents can be changed in place
a= [1,2,3,4]
b=a
b.append(8)
print(a) # a list will also change (mutable)


# is vs ==
a=7
b=7
print(a==b) # returns true ,shares same value
print(a is b) #return false different objects in memory

#fstring
name="Jinka Mahesh"
age=25
print(f"i am  {name} and I am {age} years old")

#size limit 
big=9999999999999999999999999
print(big+1) # no size limit in python

#bool( subtype of int )
print(True+True) # booleans are subtype of int True=1,false=0 #returns 2

#Chained comparisions
x=10
print(1<x<100)

#flooring
print(-7//2) # returns -4 floorin always takes left of original value

#modulo
#=(a//b)*b +(a%b)
print(-7%2) # from above formula it will return 1


# "_" are allowed in numeric literals for readability
x=1_000_000
print(x) #return 1000000

