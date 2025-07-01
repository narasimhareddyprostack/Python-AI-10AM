class Account:

    def open_account(self):
        print("Account Opened")

    def deposit_amount(self,amount):
        print(amount," :Amount Deposited")

a1=Account() 
a1.open_account()
a1.deposit_amount(50000)  
a2=Account()   