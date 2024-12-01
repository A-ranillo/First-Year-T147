class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, name):
        if isinstance(name, str) and len(name) > 10:
            self.__owner = name
        else:
            raise ValueError(f"{value} is not a string or {value} is not 10 characters long")


    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if isinstance(value, int)  and value > 0 or isinstance(value, float) and value > 0:
            self.__balance = value
        else:
            raise ValueError(f"{value} is not a number or {value} is not greater than 0")



    def __str__(self):
        return f"Bank owner: {self.owner}, Balance: {self.balance}"

    def deposit(self, amount):

        if isinstance(amount, int) and amount > 1 or isinstance(amount, float) and amount > 1:
            self.balance = self.balance + amount
            self.transactions.append(f"Deposit: ${amount}")
        else:
            raise ValueError(f"{amount} is not a number or {amount} is not greater than 1")
    def withdraw(self, amount):
        if isinstance(amount, int) and amount < self.balance or isinstance(amount, float) and amount < self.balance:
            self.balance = self.balance - amount
            self.transactions.append(f"Withdraw: ${amount}")
        else:
            raise ValueError(f"{amount} is not a number or {amount} is less than the balance")
    def display_balance(self):
        print(f"Balance: {self.balance}")
    def display_transactions(self):
        for num, transaction in enumerate(self.transactions, start=1):
            print(f"{num}) {transaction}")