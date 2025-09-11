class payment():
    
    def pay(self,amount):
        print(f"Payment of amount: {amount} made using generic payment method.")
class creditcard(payment):

    def pay(self,amount):
        print(f"Payment of amount: {amount} made using credit card.")
class upi(payment):
    def pay(self,amount):
        print(f"Payment of amount: {amount} made using UPI.")
class cash(payment):
    def pay(self,amount):
        print(f"Payment of amount: {amount} made using cash.")
cc=creditcard()
c=cash()
u=upi()
l=[cc,c,u]
for i in l:
    i.pay(int(input("Enter the amount:")))        


    