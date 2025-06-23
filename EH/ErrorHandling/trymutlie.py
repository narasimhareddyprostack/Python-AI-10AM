a=None 
fp=None
try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print("Your Numbers are",a,":",b)
    print(a/b)
    fp=open("emp.txt")
except ValueError as err:
    #print(err)
    print("buddy Please enter only digits")
except ZeroDivisionError as err:
    #print(a/1)
    print("We cant divibe by zero")
except FileNotFoundError as err:
    print("File Not Found! Please check")
except:
    pass

