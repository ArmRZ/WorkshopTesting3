class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

class MoneyTransfer:
    @staticmethod
    def transfer(sender, receiver, amount):
        # sender = account1
        sender.withdraw(amount)
        # receiver = account2
        receiver.deposit(amount)
