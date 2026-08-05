#Numeric Types
age=12 #integer
height=5.9 #float
complex_num=3+5j #complex

#textual Type
text="Mahesh" #string

#Boolean Type
is_student=True #boolean

#  None Type
result=None #NoneType

#Checking Variables Type
print(type(age))
print(type(height))
print(type(complex_num))
print(type(text))
print(type(is_student))
print(type(result))

#Dynamic typing
x=10 #integer
x="hello" # now its string 

#Type Conversion(casting)

## String to number
x="15"
y=int(x) # converts string to integer
print(type(y))

#Number to string
x=15
y=str(x) # converts integer to string
print(type(y))

#Float and integer conversion
x=15.5
y=int(x) # converts float to integer
print(type(y))
z=float(y) # converts integer to float
print(type(z))

#decimal looking string to integer
x="15.5"
y=int(float(x)) # converts string to float, then to integer
print(type(y))


#Multiple Variable Assignment
a,b,c=10,20,30 # assigns 10 to a, 20 to b, 30 to c
a=b=c=10 # assigns 10 to a,b,c

#Mutability

# Immutable types: int, float, str, tuple, bool
x=5
y=x
y=10
print(x) # prints 5, x is unchanged

# Mutable types: list, dict, set
list1=[1,2,3]
list2=list1
list2.append(4)
print(list1) # prints [1,2,3,4], list1 is changed ,Same object in memory


#memory reference
x=5
y=5
print(id(x)) # prints memory address of x
print(id(y)) # prints memory address of y, same as x

# is vs ==
a=[1,2,3]
b=[1,2,3]
print(a is b) # prints False, different objects in memory
print(a == b) # prints True, same values

#f-strings (modern way to format variables into text)
name="Mahesh"
age=12
print(f"My name is {name} and I am {age} years old.") # prints "My name is Mahesh and I am 12 years old."

#Constants (convention, not enforced)
#Python has no true constants — by convention, use ALL_CAPS to signal "don't change this":
CONSTANT_VALUE = 3.14