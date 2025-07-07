class InsuffientBalError(Exception):
    def __init__(self, msg):
        self.msg=msg 

class InsuffientSleepError(Exception):
    def __init__(self, msg):
        self.msg=msg 
