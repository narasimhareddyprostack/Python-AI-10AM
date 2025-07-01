# Extract
import requests,csv 

data=requests.get('https://dummyjson.com/users')
user_data=data.json()
print(type(user_data))  #<class,dict>
users=user_data['users']
print(len(users))       #30
print(type(users))      #<class,list>

# Transform
new_users=[]
for user in users:
    new_users.append([user['id'],user['firstName'],user['age']])
#print(new_users)


# Load
fp=open('users.csv','w',newline='')
csvwriter=csv.writer(fp)

csvwriter.writerow(['uid','uname','age'])
csvwriter.writerows(new_users)
print("New file Created")
fp.close()