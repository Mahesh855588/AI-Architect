# *Args  and KwArgs is Unpacking the elements from list,tuple or dictionaries
# we have 2 types as parameters and as arguments

# Defining in function(as parameter)
def Add(*numbers):
    return sum(numbers)
print(Add(1,2,3,4,5,6,7))

# Calling function with Args and Keyword arguments
# unpack list or tuple in to separate arguments
def Add(a,b,c):
    return a+b+c
nums=[1,2,3]
nums1=(1,2,3)
nums2={1,2,3}
nums3=dict(a=2,b=4,c=6)
nums4=dict(a="Jinka",b="Mahesh",c="Reddy")
print(Add(*nums))
print(Add(*nums1))
print(Add(*nums2))
print(Add(**nums3))
print(Add(**nums4))