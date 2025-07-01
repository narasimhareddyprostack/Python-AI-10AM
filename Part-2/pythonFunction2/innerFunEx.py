def outer():
    print("Outer fun started")

    def inner():
        print("Inner Function") 

    def login():
        print("Login Success") 

    return inner
    
inner=outer()
inner()
inner()