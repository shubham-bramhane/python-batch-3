


# with open('new.txt','r') as f:
#     new=f.read()
#     print(new)

# try:
#     f=open('new.txt','r')
#     print(f.read())
#     f.close()
# except:
#     print('file not found')

# print(10)















# f=open('new4.txt','w')
# f.write('hello i am shubham from magical umbrella private limited')
# f.close()



# try:
#     with open('new.txt','a') as f:
#         f.write(' i am going to school')

# except:
#     with open('new.txt','w') as f:
#         f.write('hello i am shubham bramhane')



# try:
#     with open('new.txt','r') as f:
#         print(f.readline())
        


# except:
#     with open('new.txt','w') as f:
#         f.write('hello shubham')




# try:
#     with open('new.txt','r') as f:
#         print(f.readlines())
        


# except:
#     with open('new.txt','w') as f:
#         f.write('hello shubham')



# try:
#     with open('new.txt','r') as f:
#         print(f.read(5))
        
# except:
#     with open('new.txt','w') as f:
#         f.write('hello shubham')


# try:
#     with open('new.txt','a') as f:
#         f.write('\npython is object oriented language')

# except:
#     print('file not exist')



# import os
# os.remove('new.txt')

import os

try:
    os.remove('new.txt')

except:
    with open('new.txt','w') as f:
        f.write('shubham')