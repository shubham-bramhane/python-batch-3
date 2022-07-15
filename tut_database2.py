from django.db import DatabaseError
import mysql.connector

# for showing databases


# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
    
# )

# mycursor=mydb.cursor()



# mycursor.execute('show databases')

# for i in mycursor:
#     print(i)



# 
#for create database 



# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
    
# )

# mycursor=mydb.cursor()



# mycursor.execute('create database python_batch_6')


# -----------------------------------------------------


# for showing table in Database



# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_5'
    
# )

# mycursor=mydb.cursor()



# mycursor.execute('show tables')

# for i in mycursor:
#     print(i)

# ---------------------------------------------



# for creating table




# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()



# mycursor.execute('create table user(id int auto_increment primary key,name varchar(255),contact varchar(255))')
# ---------------------------------------------------------



# for inserting data into table 





# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()



# mycursor.execute("insert into user(name,contact)values('shubham','8857916707')")

# mydb.commit()
# ------------------------------------------

# for select the data from table 


# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()


# mycursor.execute("select * from user")

# datas=mycursor.fetchall()



# for data in datas:
#     print(data)



# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()


# mycursor.execute("select * from user where id=4")

# datas=mycursor.fetchall()



# for data in datas:
#     print(data)





# for deleteting the data 


# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()


# mycursor.execute("delete from user where id =4")


# mydb.commit()


# foor updating the data from user 


# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='python_batch_6'
    
# )

# mycursor=mydb.cursor()


# mycursor.execute("update user set name='suraj' where id=2 ")


# mydb.commit()




# print('query executed!!!!')


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_batch_6'
    
)
mycursor=mydb.cursor()





firstname=input('enter the name')



mobile_no=input('enter the mobile number')


sql="insert into user(name,contact)values(%s,%s)"

val=(firstname,mobile_no)



mycursor.execute(sql,val)

mydb.commit()


print('data inserted successfully!!!')









# create a database that contain a table name "user" ,suer having 4 attributes i.e id,name,address,contact after that 

# show the data like 
# press 1 for inssrt the data into table
        # 
#  press 2 for delete the data into table

# press 3 for display the data into table 

# press 4 for update the data into table
#     




