unames=('Rahul','Sonia','Priyanka','Modi')
#index    0       1        2         3

#how to iterate tuple - for,while
for name in unames:
    print(name)

print(unames.index("Sonia"))  #1
#print(unames.index("Rajni"))  #ValueError

print(unames.count("Sonia"))  #1