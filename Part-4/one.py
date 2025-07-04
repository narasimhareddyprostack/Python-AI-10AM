class InsuffientBalError(Exception):
    def __init__(self, msg):
        super()
        self.msg=msg
    
def withdrawl_amount():
    amount = int(input("Enter amout to withdrawl:"))
    acc_bal = 1500
    if acc_bal<amount:
        raise InsuffientBalError("Low Bal") 
    else:
        print("Enjoy") 
    print("Please follow Rules")

withdrawl_amount()
    