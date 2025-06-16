def login_req(func):

    def inner(name,status):
        if status ==False:
            print("Login is required")
        else:
            return func(name,status)
        
    return inner
