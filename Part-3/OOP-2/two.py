class Account:
    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=amount

    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount

a1=Account(101,'Rahul',5000)
a1.deposit_amount(100)
a1.deposit_amount(200)

a2=Account(102,'Sonia',15000)
a2.deposit_amount(2500)
print(a1.__dict__)
print(a2.__dict__)