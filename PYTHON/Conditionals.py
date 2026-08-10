# If 
age=19
if age>=18:
    print("Adult")

#If else
if age>=18:
    print("Major")
else:
    print("Minor")

#If else if Else
a=11
if(a==1):
    print(" a equals 1")
elif a>1 and a<20:
    print("a is greater than 1 and less than 20")
else:
    print("a is greater than 20")


#Conditional trap 
marks=99
if marks>50:      # wrong way of representing the conditional statements
    print("Grade C")
elif marks>90:
    print("Grade A")
else:
    print("Fail")


# Correct way 
if marks>90:
    print("Grade A")
elif marks>50:
    print("Grade C")
else:
    print("Fail")


#All empty datatypes are falsy
#All non empty datatypes are truthy

#nested conditions
age=19
is_allowed=True
if age>18:
    if is_allowed:
        print("He is 18 above ,He is allowed")
    else:
        print("he is not allowed")
else:
    print("he is not above 18 he is not allowed")


#Chained comparisions
if 18<=age<=65:
    print("He is allowed to work")
else:
    print("He is not allowed")



#match condition

day=5
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("Enter correct value")


# pass keyword
#instead of using empty block we use place holder "pass" in development time

if age >=18:
    pass
