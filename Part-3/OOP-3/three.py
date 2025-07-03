class Test:
    g=70  #static variable
    def __init__(self):
        self.a=10
        self.b=20
        Test.z=100

    def m1(self):
        self.c=30
    @classmethod
    def m2(cls):
        cls.e=50   #static
        Test.h=80  #static

t1=Test()
t1.m1()
t2=Test()
t2.d=40       #instance
Test.f=60     #static
t1.m2()
print(t1.__dict__) #{'a': 10, 'b': 20, 'c': 30}
print(t2.__dict__) #{'a': 10, 'b': 20, 'd': 40}
print(Test.__dict__)