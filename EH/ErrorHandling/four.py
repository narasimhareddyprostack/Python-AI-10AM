fp=None
try:
    fp=open('emp.txt','r')    #risky code

except FileNotFoundError as err:
    fp=open('default.txt','r') 

data=fp.read()
print(data)
print("GM")
fp.close()