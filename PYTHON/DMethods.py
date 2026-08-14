'''
print(obj)      →  calls obj.__str__()
str(obj)          →  calls obj.__str__()
repr(obj)           →  calls obj.__repr__()
obj1 == obj2          →  calls obj1.__eq__(obj2)
obj1 < obj2             →  calls obj1.__lt__(obj2)
len(obj)                  →  calls obj.__len__()
obj[0]                      →  calls obj.__getitem__(0)
x in obj                      →  calls obj.__contains__(x)
obj1 + obj2                     →  calls obj1.__add__(obj2)
obj(5)                             →  calls obj.__call__(5)
if obj:                              →  calls obj.__bool__()
'''