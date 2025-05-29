list1=[80,40,81,14,255,0]

bytes_obj=bytes(list1)

#bytes_obj[3]=82  # Item assignment not possible
print(81 in bytes_obj)   #True
print(82 in bytes_obj)   #False


