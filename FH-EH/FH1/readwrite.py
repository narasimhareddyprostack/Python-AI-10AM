fp1 = open('data.txt','r')
data=fp1.read()

fp2= open('xyz.txt','a')
fp2.write(data)

print("New file Created and Written successfully")

fp1.close()
fp2.close()