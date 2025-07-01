class Employee:
    branch_code=11
    
e1=Employee()
e2=Employee()
e3=Employee()
#print - object in the form of dict
print(e1.__dict__)   #{}
print(e2.__dict__)   #{}
print(e3.__dict__)   #{}
print(Employee.__dict__)