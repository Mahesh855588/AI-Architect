# Walrus operator
# assigning the value and using the value in the same line(:=)

#old way
n=10
if n>5:
    print(n)

#Walrus
if (n:=10)>5: #assigning the value and using the value in same line
    print(n)