name="pythonis high level language"

# *
# ** 
# ***


# for i in range(10):
#     print("*"*i)



# for row in range(1,10):
#     for column in range(1,row):
#         print("*",end=' ')
#     print()
    

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
 

# for row in range(1,10):
#     num=1
#     for column in range(1,row):
#         print(num,end=' ')
#         num=num+1
#     print()



# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3
# 1 2
# 1


# for row in reversed(range(1,10)):
#     num=1
#     for column in range(1,row):
#         print(num,end=' ')
#         num=num+1
#     print()



# 1
# 2 3
# 4 5 6 
# 7 8 9 10

# num=1
# for row in range(10):
#     for column in range(row):
#         print(num,end=' ')
#         num=num+1
#     print()




# for i in range(0,100):
#     if i%2==0:
#         print(i,'is even number')
#     else:
#         print(i,'is odd number')


# 5!=5*4*3*2*1=120




# 10 20 30 40 50 60 70 80 90 100
# num=100
# for i in range(10):
#     print(num,end=' ')
#     num=num-10



# for i in range(100):
#     print(i)
#     if i==50:
#         break


# for i in range(100):
#     if i>50 and i<55:
#         continue
#     print(i)
    




# 0
# 2 4
# 6 8 10
# num=0
# for row in range(10):
#     for column in range(row):
        
#         print(num,end=' ')
#         num=num+2
#     print()


# 1 3 5 7 11 13 17 19 23 

# for i in range(1,100):
#     for j in range(1,10):
#         if i%j==0:
#             print(i)


# num=int(input('enter the number'))

# if num%2==0:
#     print(num,'prime number')
# else:
#     print('not prime number')


# 0 50 100 150 200 250 300 350 400 450 500


# for num in range(2,100):
    
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)



num=50
for i in range(1,11):
    print(num,end=' ')
    num=num+50
 