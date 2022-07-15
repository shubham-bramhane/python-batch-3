#  display database

# show databases;


# for selecting database 

# use database_name;



# for display table 

# show tables;



# for creating table 

# create table user(name varchar(255),address varchar(255));


# for showing column from user

# describe user; desc user;


# for insert the data into table 

# insert into user(name,address) value ('shubham','ghugus');



# for fechting the data 

# select * from user ;


# select name from user ;

# select * from user where name="shubham";



# for deleting the data

# delete from user where id=1;


# fro update data 

# update user set address="ghugus" where id=6;





import mysql.connector


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_batch_5'
)

mycursor=mydb.cursor()

# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)



# mycursor.execute('create table contact(id int auto_increment primary key,name varchar(255),phone_no int(10))')


# print('query executed!!!!')




mycursor.execute("insert into contact(name,phone_no) values('shubham','8857916707')")

mydb.commit()

print('query executed!!!')