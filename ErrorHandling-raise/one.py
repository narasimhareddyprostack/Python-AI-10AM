from errors import InsuffientBalError

def withdrawl_amount():
    amount=int(input("Enter Amount for Withdrawl:"))
    #fetch acc_bal from database
    acc_bal = 5000
    if acc_bal<=amount:
        raise InsuffientBalError("Account Bal is low - Earn now") 
    else:
        print("Enjoy!")
    
    print("Follow Rules")

withdrawl_amount()