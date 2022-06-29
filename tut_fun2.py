





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
#      print('invalid choice!!!!')


# mydata=[]
# temp=int(input('how many value insert into list'))
# for i in range(temp):
#     print('enter the',i+1,'of',temp, "value:")
#     mydata.append(int(input()))



# print('press 1 for min value')
# print('press 2 for max value')
# print('press 3 for average value')
# choice=int(input('enter your choice'))
# if choice==1:
#     print('-----choice 1 selected------')
#     mydata.sort()
    
#     print('the minimum value is',mydata[0])
# elif choice==2:
#     print('-----choice 2 selected------')
#     mydata.sort(reverse=True)
    
#     print('the maximum value is',mydata[0])
# elif choice==3:
#     print('-----choice 3 selected------')
#     no_of_mydata=len(mydata)
#     sum=0
#     for i in mydata:
#         sum=sum+i
    
#     average=sum/no_of_mydata

#     print('average is',average)

# else:
#     print('invalid value!!!!!!')



# mydata=[]
# temp=int(input('how many value insert into list'))
# for i in range(temp):
#     print('enter the',i+1,'of',temp, "value:")
#     mydata.append(int(input()))





# print('press 1 for min value')
# print('press 2 for max value')
# print('press 3 for average value')
# print('press 4 for exit')
# choice=int(input('enter your choice'))
# while(choice>=1):

#     if choice==1:
#         print('-----choice 1 selected------')
#         mydata.sort()
        
#         print('the minimum value is',mydata[0])
#         choice=int(input('enter your choice'))
        
#     elif choice==2:
#         print('-----choice 2 selected------')
#         mydata.sort(reverse=True)
        
#         print('the maximum value is',mydata[0])
#         choice=int(input('enter your choice'))
#     elif choice==3:
#         print('-----choice 3 selected------')
#         no_of_mydata=len(mydata)
#         sum=0
#         for i in mydata:
#             sum=sum+i
        
#         average=sum/no_of_mydata

#         print('average is',average)
#         choice=int(input('enter your choice'))
#     elif choice==4:
#         print('you are exit !!!!')
#         break

#     else:
#         print('invalid value!!!!!!')
#         break
    



# mydata=[]
# temp=int(input('how many value insert into list'))
# for i in range(temp):
#     print('enter the',i+1,'of',temp, "value:")
#     mydata.append(int(input()))





# print('press 1 for min value')
# print('press 2 for max value')
# print('press 3 for average value')
# print('press 4 for exit')
# choice=int(input('enter your choice'))
# while(choice>=1):

#     if choice==1:
#         print('-----choice 1 selected------')
#         mydata.sort()
        
#         print('the minimum value is',mydata[0])
#         choice=int(input('enter your choice'))
        
#     elif choice==2:
#         print('-----choice 2 selected------')
#         mydata.sort(reverse=True)
        
#         print('the maximum value is',mydata[0])
#         choice=int(input('enter your choice'))
#     elif choice==3:
#         print('-----choice 3 selected------')
#         no_of_mydata=len(mydata)
#         sum=0
#         for i in mydata:
#             sum=sum+i
        
#         average=sum/no_of_mydata

#         print('average is',average)
#         choice=int(input('enter your choice'))
#     elif choice==4:
#         print('you are exit !!!!')
#         break

#     else:
#         print('invalid value!!!!!!')
#         break
    
    
    
from itertools import count

for i in count(0):
    print('press 1 for min value')
    print('press 2 for max value')
    print('press 3 for average value')
    print('press 4 for exit')
    choice=int(input('enter your choice'))
    if choice==1:
        print('----choice 1 selected-------')
        choice=int(input('enter your choice'))
    
    if choice==2:
        print('----choice 2 selected-------')
        choice=int(input('enter your choice'))
    
    if choice==3:
        print('----choice 3 selected-------')
        choice=int(input('enter your choice'))
    
    if choice==4:
        print("exit!!!")
        break

    else:
        print('invalid choice')
        choice=int(input('enter your choice'))

    




 
    





