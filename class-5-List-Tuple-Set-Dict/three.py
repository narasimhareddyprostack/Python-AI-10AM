enames=["RG","SG","PG","NM","AS"]
#index    0    1    2   3     4
#-ve Indexing possible

#read list element - using index
print(enames[0])   #RG
print(enames[1])
print(enames[2])
print(enames[3])
print(enames[4])  #AS
#print(enames[15]) #IndexError

#upate
enames[0] = "Mr .Rahul Gandhi"
print(enames)

#delete 
del enames[4]

#read
print(enames)