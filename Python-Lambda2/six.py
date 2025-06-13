numbers=[37,18,31,14,8,12,7]

def check_odd(num):
    return num%2 !=0

odd_no=list(filter(check_odd,numbers))

print(numbers)
print(odd_no)