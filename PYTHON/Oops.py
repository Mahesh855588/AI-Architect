# Object oriented programming

#Class 
#class is a template or blueprint which contains data(attribute) and methods performing operations on the data

#self
# self represent current instance of an object

#__init__
# when we create an instance of class __init__ method will be called by default to assign attributes  directly to the class

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Hi this is {name} and i am {age} years old !")
p1=Person("mahesh",25)
p2=Person("saiteja",29)


# Bank account

class Bank:
    def __init__(self,accountHolder,balance):
        self.accountHolder=accountHolder
        self.balance=balance
    def Withdraw(self,amount):
        if(amount>self.balance):
            print(f"we are sorry  your {self.balance} is less than the entered {amount}/-")
        else:
            print(f"successfully withdrwan {amount} and remaining balance is {self.balance-amount}/-")
    def Deposit(self,amount):
        self.balance+=amount
        print(f" deposited successfully\n your current balance is {self.balance+amount}")

account=Bank("Mahesh",10000)
account.Deposit(1000)
account.Withdraw(2000)