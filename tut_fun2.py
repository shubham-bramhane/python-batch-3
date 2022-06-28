





# def tringle(x,star):
#     for row in range(1,x+1):
#         num=star
#         for column in range(row):
#             print(num,end=' ')

#         print()




# def rev_tringle(x,star):
#     for row in reversed(range(1,x+1)):
#         num=star
#         for column in range(row):
#             print(num,end=' ')

#         print()




# print('press 1 for normal tringle')
# print('press 2 for reverse tringle')
# choice=int(input('enter your choice'))
# if choice==1:
    
#     temp=int(input('enter the value'))
#     star=input('what you print')
#     tringle(temp,star)
# elif choice==2:
    
#     temp=int(input('enter the value'))
#     star=input('what you print')
#     rev_tringle(temp,star)

# else:
#     print('invalid choice!!!!')
mydata=[]
# temp=int(input('how many value insert into list'))
# for i in range(temp):
#     print('enter the',i+1,'of',temp, "value:")
#     mydata.append(int(input()))


print(mydata)
print('press 1 for min value')
print('press 2 for max value')
print('press 3 for average value')
choice=int(input('enter your choice'))
if choice==1:
    print('-----choice 1 selected------')
    
    print(mydata.sort())
elif choice==2:
    print('-----choice 2 selected------')
elif choice==3:
    print('-----choice 3 selected------')
else:
    print('invalid value!!!!!!')








