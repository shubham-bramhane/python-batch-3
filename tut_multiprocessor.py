import multiprocessing




def square():
    for i in range(1000):
        print('sqaure of',i,'is',i*i)




def cube():
    for i in range(1000):
        print('cube of',i,'is',i*i*i)




# p1.join()
# p2.join()

if __name__ == '__main__':



    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)

    
    p1.start()
    p2.start()


    print('hello')