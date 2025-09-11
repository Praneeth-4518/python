class bankacc:
    __bal = 0
    def deposit(self, amount):
        self.__bal += amount
    def withdraw(self, amount):
        if amount > self.__bal:
            print("Insufficient balance")
        else:

            self.__bal -= amount
    def get_balance(self):
        print(f"Balance is:{self.__bal}")        
acc=bankacc()
acc.deposit(5000)
acc.withdraw(2000)  
acc.get_balance()
class savingsacc(bankacc):
    def display(self):
        print(super.__bal)
s=savingsacc()
s.display()        