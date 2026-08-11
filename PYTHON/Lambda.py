#Lambda functions are tiny functions which are used in throw away conditions

#Rules:
# should be one line function
# no if/else blocks only use ternary operator
# no more than 1 expression
# cant have doc strings and type hints

#syntax  (lambda arguments:expression)

square=lambda x:x**2
print(square(5))

Add=lambda a,b:a+b
print(Add(3,4))

string=lambda name="guest":f" Hello {name}"
print(string())
print(string("Mahesh"))

eveOdd=lambda x:"even" if x%2==0 else "Odd"
print(eveOdd(7))

#sorted()-list
lst=["apple","banana","cat","dog"]
result=sorted(lst,key=lambda x:len(x))
print(result)

#sorted()-list of tuples
lt=[("apple",9),("banana",87),("cat",56)]
result=sorted(lt,key=lambda a:a[1])
print(result)

#sorted()-dictionaries
di=dict(apple=78,banana=76,orange=65)
result=sorted(di.items(),key=lambda x:x[1])
print(result)

#sorting()-multiple keys
lt=[("apple",90,"G"),("banana",87,"B"),("cat",56,"A")]
result=sorted(lt,key=lambda x:(x[1],x[2]))
print(result)


#map()
m=[1,2,3,4,5]
result=map(lambda x:x**2,m)
print(list(result))

#filter()
f=[1,2,3,4,5,6,7]
result=filter(lambda x:x%2==0,f)
print(list(result))


#invoked lambda
result=(lambda x,y:x+y)(5,6)
print(result)