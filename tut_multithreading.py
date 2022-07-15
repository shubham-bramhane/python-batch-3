# import time
# st=time.time()




# def square():
#     for i in range(100000):
#         print('sqaure of',i,'is',i*i)




# def cube():
#     for i in range(100000):
#         print('cube of',i,'is',i*i*i)




# square()
# cube()


# et=time.time()


# print(et-st)




# import threading
# import time

# st=time.time()


# def square():
#     for i in range(100000):
#         print('sqaure of',i,'is',i*i)




# def cube():
#     for i in range(100000):
#         print('cube of',i,'is',i*i*i)






# obj1=threading.Thread(target=square)

# obj2=threading.Thread(target=cube)


# obj1.start()
# obj2.start()
# obj1.join()
# obj2.join()

# et=time.time()


# print(et-st)


# 1
# 1 2 
# 1 2 3


import threading

import time


st=time.time()

def tringle(x):
    for row in range(x):
        num=1
        for column in range(row+1):
            print(num,end=' ')
            num=num+1
        print()



def reverse_tringle(x):
    for row in reversed(range(x)):
        num=1
        for column in range(row+1):
            print(num,end=' ')
            num=num+1
        print()




# reverse_tringle(10)
# tringle(10)




obj=threading.Thread(target=tringle,args=(10,))

obj2=threading.Thread(target=reverse_tringle,args=(10,))


obj.start()
obj2.start()


obj.join()
obj2.join()


et=time.time()

print(et-st)
# 0.017994403839111328
