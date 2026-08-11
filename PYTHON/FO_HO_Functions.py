#first order functions
# these functions are used as any other values
#stored in variables ,lists,sets etc
#returned from other function
def Greet():
    return "Hello Mahesh"
greeting=Greet
print(greeting())
lst=[1,2,Greet,4]
print(lst[2]())
di=dict(name=Greet)
print(di["name"]())


#Higher order functions
#Takes another function as an argument (map(),sorted(),filer(),reduce())
#returns a function as its result
def Apply(Func,value): #function as argument
    return Func(value)
def Add():
    x=12 #enclosed scope
    def Sub():
        return x
    return Sub #return function as its result
result=Add()
print(result())

from functools import reduce
#reduce() repeatedly applies a function to pairs of items, "reducing" the whole list down to one value: ((1+2)+3)+4 = 10
nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)   # 10


# event handlers or callbacks
def OnSuccess():
    print("Task completed successfully..")
def OnFailure():
    print("Task failed")

def RunTask(success,Failure):
    try:
        success()
    except Exception:
        Failure()
RunTask(OnSuccess,OnFailure)