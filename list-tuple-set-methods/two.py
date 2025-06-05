#create
enames=["RG","SG","PG","RG"]

#index method - return index value of first occurance of element
print(enames.index("RG"))     #0
#print(enames.index("Rajni"))  #ValueError: 'Rajni' is not in list

#count method- return no of occurances
print(enames.count("RG"))   #2
print(enames.count("Rajni")) #0