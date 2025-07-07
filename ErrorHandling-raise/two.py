from errors import InsuffientBalError
def withdrawl_amount():
    amount = int(input("Enter Amount to withdrawl:"))
    #get bal from DB
    acc_bal = 5000
    try:
        if acc_bal<=amount:
            raise InsuffientBalError("Bal is Low! Earn Now!")
        else:
            print('Enjoy')
    except InsuffientBalError as err:
        print(err.msg)

    print("Follow Bank Rules")

withdrawl_amount()