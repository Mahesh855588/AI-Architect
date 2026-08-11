# closure is a function that remembers variables from the scope it was created in (enclosing scope) even after outer loop completes
def Add():
    x=5
    def Sub():
        print(x)
    return Sub
result=Add()
result() # x is still accesible even after outer loop  already returned
#print(x) # this will throw error ,x is not global , x will be in pocket of Sub function

