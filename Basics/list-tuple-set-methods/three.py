#create
enames=["RG","SG","PG","RG"]
#append - appeding element eod of list
enames.append("NM")
print(enames)  #['RG', 'SG', 'PG', 'RG', 'NM']

#insert - insert specified object @ specified index
enames.insert(3,"VK")

print(enames)  #['RG', 'SG', 'PG', 'VK', 'RG', 'NM']