list1=[80,40,81,14,255,0]
ba=bytearray(list1)
print(type(ba))

ba[1] =41    #Item Assignment Possible, Mutable Object
print(ba)    #address
print(81 in ba)   #True

for value in ba:
    print(value)
