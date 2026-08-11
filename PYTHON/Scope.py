# scope determines where a variable can be seen and  where to use

#Local scope
# values defined inside function
def Add():
    a=10
    return a+a
print(Add())

#Global scope
# Values defined at top of the script or module
x=80
def Add():
    return x+x
print(Add())

#Enclosing scope
#defined inside outer loop and outside inner loop and used in inner loop
def Add():
    y=90
    def Sub():
        print(y)
    return Sub()
Add()

# built in scope
#print,len,range etc
print(len([1,2,4,5,6,7]))