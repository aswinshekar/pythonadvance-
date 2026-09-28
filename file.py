# # f=open('k.txt','w')
# # f.write("hello\n")
# # f.writelines(['hello\t','python\n'])
# # f.close()
#
# # write a pgm to append the contents from from file into another text file
# #
# # f1=open("k.txt", "r")
# # data = f1.read()
# #
# # f2=open("file2.txt", "a")
# # f2.write(data)
#
#
#
# # f1 = open("k.txt", "r")
# # f2 = open("file2.txt", "a")
# # data = f1.readlines()
# # for i in data:
# #     f2.write(i)
# # f1.close()
# # f2.close()
#
#
# # f=open("k.txt",'r')
# # s=f.read()
# # f.close()
# #
# # f=open("file2.txt",'a')
# # f.write(s)
# # f.close
#
#
#
# # f=open("file2.txt",'a+')
# # print(f.tell())
# # f.write("world")
# # print(f.tell())
# # f.seek(0)
# # print(f.tell())
# # print(f.read())
#
#
#
def read():
    fi = input("ENTER THE FILE NAME ")
    f = open(fi, 'r')
    print(f.read())

def write():
    fi = input("ENTER THE FILE NAME ")
    f = open(fi, 'w')
    d = input("ENTER DATA: ")
    f.write(d)
    f = open("k.txt", 'r')
    print(f.read())

def append():
    fi = input("ENTER THE FILE NAME ")
    f = open(fi, 'a+')
    d = input("ENTER DATA: ")
    f.write(" " +d)

def search():
    fi = input("ENTER THE FILE NAME ")
    f = open(fi, 'r')
    d = input("ENTER WORD TO SEARCH: ")
    c = f.read()
    if d in c:
        print("WORD IS FOUND")
    else:
        print("WORD IS NOT FOUND")
def delete():
    fi = input("ENTER THE FILE NAME ")
    import os
    os.remove(fi)

while(1):
    print("------------------------------------------")
    print("\n 1.FILE READ \n 2.FILE WRITE \n 3.FILE APPEND\n 4.FILE SEARCH \n 5.FILE DELETE \n 6.EXIT \n ")
    print("------------------------------------------")
    i = int(input("ENTER YOUR CHOICE: "))
    if i==1:
        read()
    elif i==2:
        write()
    elif i==3:
        append()
    elif i==4:
        search()
    elif i==5:
        delete()
    elif i==6:
        exit()
    else:
        print("\nENTER A VALID NUMBER")




