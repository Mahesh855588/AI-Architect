#Operator precedence
    #rule exponentiaiton-unary operator-> * -> / -> // -> + -> - -> comparisions -> not -> and -> or
#exponentiation is right assosiative(left to right)
# 2**(3**2) = 2**9 =512
print(2**3**2) 

#arithmetic operators
a=10
b=29
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(b%a)


#comparision operators
a=20
b=77
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#logical operators
a=True
b=False
print(a and b)
print(a or b)
print(not b)

#assignment operators
a=5
b=7
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a%=b
print(a)


#membership operator
a=[1,2,3,4,5]
print(1 in a)
print(2 not in a)


#Walrus operator
if (a:=8)>5:
    print(a) #prints 8 if a > 5


#augmented operator
a=[1,2,3,4,5]
b=a
a+=[6]
print(b) # this will change b

a=[1,2,3,4]
b=a
a=a+[6]
print(b) # this will not change b (agmented operator)


#bit wise operators
a=5
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<1)
print(a>>1)
print(~a)




