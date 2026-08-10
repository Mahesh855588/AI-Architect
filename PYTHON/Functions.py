# defining and calling a function
def Func():
    print("Hello World")
Func()

#Parameter and argument
# place holder in function definition is parameter
# actual value you pass  in when calling is argument

def ParaArg(name):
    print(f"This is {name}")
ParaArg("Mahesh")


# Return
# return sends value back whereever the function was called
def AddWithReturn(a,b):
    return a+b
result=AddWithReturn(5,6)
print(result)

# If we don't return it will send "None"
def AddWIthOutReturn(a,b):
    a+b
result=AddWIthOutReturn(7,8)
print(result)

# Default parameter values
# Default parameters should always be immutable its better to keep None 
def DefaultParameterValues(name="Jinka"):
    print(f"this is {name}")
DefaultParameterValues() #prints Jinka with no arguments
DefaultParameterValues("Mahesh") #prints with mahesh

def AddItem(item,lst=None):
    if lst is None:
        lst=[]
    lst.append(item)

    return lst
result=AddItem(7)
print(result)

#Positional arguments
def Describe(name,age):  
    print(f"I am {name} and I am {age} years old")
Describe("Mahesh",25) #These are positional arguments and should be in order
#If we change the order it will throw error when datatype changes

#Keyword arguments
Describe(name="Mahesh",age=25)
Describe(age=26,name="Jinka")
#Both works with keywords
#Keyword and positional mixed need correct order
Describe("Reddy",age=65)


# *args
# Accepts any number of positional arguments

def Total(*nums):
    return sum(nums)
result=Total(1,2,3,4,5,6,7,8)
print(result)


# **kwArgs
#Accepts any number of Keyword arguments
def GetInfo(**info):
    for i,j in info.items():
        print(f"{i} : {j}")
    print(info)
GetInfo(name="Mahesh",age=36,native="Nadimiburuju")


# *Args and **KwArgs
def DescribeArgs(a,b,*Args,**KwArgs):
    print(a,b)
    print(Args)
    print(KwArgs)
DescribeArgs(1,3,6,7,8,name="Mahesh",age=368)

# Unpacking arguments when calling a function
def Unpack(a,b,c):
    return a+b+c
nums=[1,2,3]
result=Unpack(*nums)
print(result)

#Multiple return Types
def MultipleRT(*nums):
    return min(nums),max(nums)
min,max=MultipleRT(1,2,3,4,5,6,7)
print(min,max)


#DocStrings
#documenting what a function does
def Doc():
    '''This is for doc string reference'''
    print("My name is mahesh")
print(Doc.__doc__)
help(Doc)

#functions reference
def Square(x):
    return x**2
def Apply(func,value):
    return func(value)
print(Apply(Square,5))


# Local vs Global variables
x=90  #global variable
def Global():
    print(x)
Global()
def Local():
    x=10 #local variable
    print(x)
Local()
def LocalGlobal():
    global x
    x=50 #changing global x to 50
    print(x)
LocalGlobal()


#recursive function 
#A functoin calling itself
def Factorial(n):
    if n<=1:
        return 1
    return n*Factorial(n-1)
print(Factorial(10))