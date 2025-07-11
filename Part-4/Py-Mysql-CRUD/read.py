import mysql.connector
sql_st='''
        select *from users;
       '''
#read mysql - users table data
dbcon=None
try:
    dbcon =mysql.connector.connect(host='localhost',user='root',password='root',
                                   database='dbone')
    cursor=dbcon.cursor()
    cursor.execute(sql_st)
    users=cursor.fetchall()
    #print(type(user))
    print(users)
    for user in users:
        print(user[1])
except mysql.connector.errors.Error as err:
    print(err)