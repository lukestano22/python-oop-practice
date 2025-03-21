class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        print(self.__balance)
        return self.__balance
    
my_account = BankAccount(int(input("How much do you have to start $")))
my_account.deposit(int(input("How much do you want to deposit $")))
my_account.get_balance()