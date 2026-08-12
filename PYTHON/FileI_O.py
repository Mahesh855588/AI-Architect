##opening and reading a file
#with closing manually
#If we are  manually opening file we have to close file

import os
print(os.getcwd()) #get current directory

f=open("data.txt","r") #read
content=f.read()
print(content)
f.close() # we have to call close() is we are not using with keyword

#with statement
#without manually closing if we use with keyword it will close automatically
#best practice
with open("data.txt","r") as f:
    content=f.read()
    print(content)

#file modes
"r"    # read (default) — file must exist
"w"    # write — creates file if missing, OVERWRITES if it exists
"a"    # append — creates file if missing, adds to the END if it exists
"x"    # exclusive create — fails if file already exists
"r+"   # read and write
"rb"   # read binary (images, etc.)
"wb"   # write binary


#reading in different ways

with open("data.txt","r") as f:
    content=f.readlines()
    print(content)

with open("data.txt","r") as f:
    for i in f:
        print(i.strip())
#writing
with open("data1.txt","w") as f: #read and write
    f.write("Hello world\n")
    f.write("Hello Mahesh\n")

#writing and reading
with open("data1.txt","r+") as f: #read and write
    f.write("world\n")
    f.write("Mahesh\n")
    content=f.read()
    print(content)

#appending
with open("data1.txt","a") as f: #read and write
    f.write("Jinka\n")
    f.write("Mahi\n")


#writing multiple liines at once
lst=["Jinka","Mahesh","reddy"]
with open("data2.txt","w") as f:
    f.writelines(lst)


#checking if file exits before opening
if os.path.exists("data.txt"):
    with open("data.txt","r") as f:
        content=f.read()
        

#exception
try:
    with open("data4.txt","r") as f:
        pass
except FileNotFoundError as e:
    print(f"exception is {e}")

# working with csv files
with open("data.csv","r") as f:
    for i in f:
        result=i.strip().split(",")
        print(result)

# reading and writing json files

import json
data={"a":1,"b":2}
with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    print(json.load(f))
