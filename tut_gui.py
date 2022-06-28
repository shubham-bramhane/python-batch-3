# # a=10
# # b=15

# # c=a+b
# # print(c)



# # d=10
# # e=11
# # f=d+e
# # print(f)



# # def add(a,b):
# #     c=a+b
# #     return c


# # print(add(5,6))
# # print(add(10,12))




# def formula(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     divi=a/b
#     print('addition is',add)
#     print('substraction is',sub)
#     print('mul is',mul)
#     print('division is',divi)



# # 1,1
# # 1,2
# # 1,3
# # 1,4
# # 1,100


# for i in range(1,100):
#     print('for ',i,'case')
#     formula(1,i)
#     print('----------------')


# def even(num):
#     if num%2==0:
#         print(num,'is even number')
#     else:
#         print(num,'is odd number')


# # for i in range(0,100):
# #     even(i)


# mylist=[]

# def add_in_list(x):
#     mylist.append(x)

# def remove(x):
#     mylist.remove(x)

# for i in range(100):
#     add_in_list(i)



# print(mylist)



# 5!=5*4*3*2*1=120
# 4i=4*3*2*1=24


# def factorial(x):
#     fact=1
#     for i in range(1,x+1):
#         fact=fact*i
#     print('factorial of',x,'=',fact)


# for i  in range(1,100):
#     factorial(i)




#swapping


# a=5
# b=6
# print('before swapping a=',a)
# print('before swapping b=',b)

# c=a+b
# a=c-a
# b=c-b

# print('after swapping a=',a)
# print('after swapping b=',b)


# 0 1 1 2 3 5 8 13 21 

temp=[0,1]

for i in range(1,10):
    temp[i-1]=i+temp[i-1]
    