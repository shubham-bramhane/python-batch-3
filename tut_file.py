


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



try:
    with open('new.txt','r') as f:
        print(f.read())

except:
    with open('new.txt','w') as f:
        f.write('hello i am shubham bramhane')

