
class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account=Bankaccount(30000)
account.deposit(2500)
print("balance",account.get_balance())