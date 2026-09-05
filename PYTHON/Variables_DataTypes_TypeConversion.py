#Numeric Types
age=12 #integer
height=5.9 #float
complex_num=3+5j #complex


# Numbers
x=2**100
print(x) # prints 1267650600228229401496703205376 since there is no overflow in python 

#IEEE-754 pitfalls(rounding issues)
print(0.1+0.2) # 0.30000000000000004  -- NOT 0.3
print(0.1 + 0.2 == 0.3)   # False
# This isn't a Python bug — it's binary floating point. 0.1 has no exact binary representation.
#practical fix --never use == for float
import math
print(math.isclose(0.1+0.2,0.3))
#another classical pitfall
#solution for above problem
from decimal import Decimal
print(Decimal("0.1")+Decimal("0.2")) #prints 0.3 we have to give in string format else will change output
print(Decimal(0.1)) #prints 0.1000000000000000055511151231257827021181583404541015625
print(Decimal("0.1"))
amount=0.0
for i in range(10):
    amount+=0.1
print(amount)  #  0.9999999999999999, not 1.0

z=3+4j #complex
print(z.real,z.imag)
print(abs(z)) #5.0  -> magnitude, via Pythagorean theorem


#fractions
from fractions import Fraction
f=Fraction(1,3)
print(f) # 1/3
print(f+Fraction(1,6))  # 1/2  -- exact, no rounding at all
print(Fraction(0.5))  # 1/2 -- floats that ARE exact in binary convert cleanly

#textual Type
text="Mahesh" #string

#Boolean Type
is_student=True #boolean
#bool is-A int in python
print(True == 1)     # True
print(False == 0)    # True
print(True + True)   # 2  -- booleans can be summed like ints!
print(isinstance(True, int))  # True -- bool IS-A int in Python

scores = [85, 42, 90, 30, 77]
passing = [s >= 50 for s in scores]
print(passing)           # [True, False, True, False, True]
print(sum(passing))      # 3 -- True counts as 1, so sum() counts how many passed

#  None Type
result=None #NoneType

#Checking Variables Type
# here variable has no type (it was like var for every variable in c#)
# whatever we assign that will be the variable
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
#cannot convert to int directly from decimal looking string, need to convert to float first


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
# (==) refers to wheather both variables have same values
# (is) refers to wheather both variables points to same object in memory 
# immutable data types with same values share same object in memory
x=98
y=98    
a=[1,2,3]
b=[1,2,3]
c=a
print(a is b) # prints False, different objects in memory
print(a == b) # prints True, same values
print(a is c) #prints true since bith variables share same location
print(x is y) # prints true since x and y are immutable

#f-strings (modern way to format variables into text)
name="Mahesh"
age=12
print(f"My name is {name} and I am {age} years old.") # prints "My name is Mahesh and I am 12 years old."

#Constants (convention, not enforced)
#Python has no true constants — by convention, use ALL_CAPS to signal "don't change this":
CONSTANT_VALUE = 3.14