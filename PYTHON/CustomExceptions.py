# Generic exceptions 
# these exceptions does not communicate what kind of problem is this
# ex ValueError,TypeError,KeyError etc

#raise ValueError("Insufficient funds")

#Custom exceptions
# immediately clears specific domain exceptions clearly
#raise InsufficientFundsError("Insufficient funds")
class InsufficientFunds(Exception): #Insufficient funds class is custom exception which inherits Exception class
    pass

def WithdrawMoney(amount,balance):
    if balance<amount:
        raise InsufficientFunds("sufficient balance not found to withdraw!")
    return balance

try:
    WithdrawMoney(400,100)
except InsufficientFunds as e:
    print(f"Transaction failed {e}")


# custom attributs or behaviour with __init__
class InsufficientFund(Exception):
    def __init__(self,amount,balance):
        self.amount=amount
        self.balance=balance
        message=f"Tried to withdraw {amount} but balance is only {balance}"
        super().__init__(message) # this message will be assigned to *args of parent class

try:
    raise InsufficientFund(500,100)
except InsufficientFund as e:
    print(e) # when print() is calles str() is called which is not present in chaild class ,so it searches in parent class which will print the message
    print(e.amount) #here e is InsuffientFund class
    print(e.balance)


#example

class BankError(Exception):
    pass
class InsufficientFundsInAcc(BankError):
    pass
class AccountFrozen(BankError):
    pass

def BankAccount(status,amount,balance):
    if status=="NonActive":
        raise AccountFrozen("account got freezed")
    if amount>balance:
        raise InsufficientFundsInAcc("There are no sufficient funds in account")

try:
    BankAccount("NonActive",500,100)
except BankError as e:
    print(f"this is bank exception {e}")

# alternative
try:
    BankAccount("Active",500,100)
except InsufficientFundsInAcc as e:
    print(f"this is bank exception {e}")
except AccountFrozen as e:
    print(f"this is bank exception {e}")