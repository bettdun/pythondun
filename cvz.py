# it restrict access to certain attributes
# methods to prevent direct modification
class Bankaccount:
    def __init__(self,balance):
        self.__balance
    def deposite(self,amount):
        if amount > 5 and amount <= 100000:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

account=Bankaccount(20000)
account.deposite(5000)
print("balance",account.get_balance())