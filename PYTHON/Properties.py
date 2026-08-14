class BankAccount:
    bank_name = "Python National Bank"    # class attribute — shared by all accounts
    minimum_balance = 0                    # class attribute — the rule for all accounts

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance             # underscore = "internal", access via property

    # ---------- REGULAR METHOD ----------
    # Needs self, because it acts on THIS specific account's data
    def deposit(self, amount):
        self._balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self._balance}")

    # ---------- @property ----------
    # Lets you read balance like an attribute, but with logic underneath
    @property
    def balance(self):
        return self._balance

    # ---------- @property.setter ----------
    # Lets you WRITE to balance like a normal attribute, but with validation
    @balance.setter
    def balance(self, value):
        if value < self.minimum_balance:
            raise ValueError(f"Balance cannot go below {self.minimum_balance}")
        self._balance = value

    # ---------- @staticmethod ----------
    # Doesn't need self OR cls — just a utility function, grouped here because it's RELATED to accounts
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # ---------- @classmethod ----------
    # Needs cls, not self — used here as an ALTERNATIVE constructor
    @classmethod
    def open_zero_balance_account(cls, owner):
        return cls(owner, balance=0)


# ============ USING ALL FOUR TOGETHER ============

# Regular constructor
acc1 = BankAccount("Mahesh", 1000)

# Regular method — needs self, acts on acc1's own data
acc1.deposit(500)
# Mahesh deposited 500. New balance: 1500

# @property — READ like a plain attribute, no parentheses
print(acc1.balance)
# 1500

# @property.setter — WRITE like a plain attribute, but validation runs underneath
acc1.balance = 2000
print(acc1.balance)
# 2000

acc1.balance = -50   # ❌ raises ValueError — the setter's validation catches this

# @staticmethod — called on the CLASS, doesn't need any specific account
print(BankAccount.is_valid_amount(500))    # True
print(BankAccount.is_valid_amount(-10))     # False

# @classmethod — an alternative way to CREATE an account, using cls
acc2 = BankAccount.open_zero_balance_account("Asritha")
print(acc2.owner, acc2.balance)
# Asritha 0