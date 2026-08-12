# Exception Handling
# The way of signalling something wrong while running the program
# excepts run time errors
# without handling it will crash

# ZeroDivisionError
#Normal
# a=45/0
# print("This is zero division error") # the program crahses in line 8 and will not execute this line
#Exception Handling
try:
    a=45/0
except ZeroDivisionError:
    print("This is zero division error") # now this line prints because of exception in line 12


#Catching the exception object itself
try:
    x=76/0
except ZeroDivisionError as e: # e object catches the exception
    print(f" this is {e} exception")

# Catching multiple exception Types and object catching the exception
try:
    a=int("abd")
except ZeroDivisionError as e:
    print(f"this is {e} exception")
except ValueError as e:
    print(f"This is {e} exception")
except TypeError as e:
    print(f"This is {e} exception")

# catching exception in one line
try:
    a=int("sjhf")
except (ZeroDivisionError,ValueError,TypeError) as e:
    print(f"This is {e} exception in one line")

# All specific exceptions will derived from Exception(parent) class which will catch all exceptions
try:
    definefunciton()
except Exception as e:
    print(f"This is {e}")

# else
# as like for and while it breaks loop ,will not execute else similarly if without exception executes else loop
try:
    print("Hi")
except Exception as e:
    print(f"This is {e}")
else:
    print("there is no exception")

# finally 
# always exceutes no matter what
try:
    x=546/0
except Exception as e:
    print(f"this is {e}")
finally:
    print("This always exceutes error or not")


# raise
# raising our own exceptions
def Account(amount,balance):
    if amount>balance:
        raise ValueError("Insufficient funds")
try:
    Account(500,100)
except Exception as e:
    print(f"you have  {e}")


# common built in exceptions
'''
ValueError       # wrong value type/format (int("abc"))
TypeError          # wrong type used in an operation ("2" + 2)
ZeroDivisionError    # dividing by zero
IndexError             # list index out of range
KeyError                 # dictionary key doesn't exist
FileNotFoundError          # trying to open a file that doesn't exist
AttributeError               # calling a method/attribute that doesn't exist on an object
'''

#logging
try:
    x=int("abc")
except Exception as e:
    print("hello")
    raise RuntimeError("please enter correct data type as input") 