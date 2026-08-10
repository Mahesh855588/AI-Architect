# For loop
for i in range(10):
    print(i)

fruits=["apple","banana","guava"]
for fruit in fruits:
    print(fruit)


#  Range() variations
print(list(range(5))) #0,1,2,3,4
print(list(range(2,5))) # 2,3,4
print(list(range(0,20,2))) #(start,stop,step)
print(list(range(0,10,-1))) #negative step from last to first


# while 
#until condition mets it will loop
count=0
while count<=5:
    print(count)
    count+=1



#Break 
# Exit the loop immmediately
for i in range(10):
    if(i==5):
        break
print(f"break {i}")

#continue 
# skip to next loop
for i in range(10):
    if(i%2==0):
        continue
    else:
        print(i)


# else on loops
for i in range(5):
    print(i)
else:
    print("loop executed succefully")

#if loop breaks in between skips else loop
for i in range(5):
    if i==3:
        break
else:
    print("loop executed successfully without breaking")



# Nested loops
for i in range(5):
    for j in range(5):
        print(i,j)


# enumerate()
#along with items it will return the position of item
vowels=['a','e','i','o','u']
for i,x in enumerate(vowels):
    print(i,x)


# zip()
# if we have 2 related lists that goes together then we use zip()

#Normal way
names=["Jinka","mahesh","reddy"]
marks=[90,90,99]
for i in range(len(names)):
    print(names[i],marks[i])

#zip()
for i,j in zip(names,marks):
    print(i,j)


# Dictionaries
d=dict(a=1,b=2,c=3,d=4)
for i,j in d.items():
    print(i,j)


# else with while
# if loop completes without breaking it will execute else loop similar as for loop with else
count=0
while count<=5:
    print(count)
    count+=1
else:
    print("loop completed successfully")



#Infinite loop protection
# if using while True condition make sure using break in inner loops

# string loop
for i in "Hello":
    print(i)

#Reversed iteration with reverse()
for i in reversed(range(10)):
    print(i)