
def read():
    try:
        fi = input("ENTER THE FILE NAME ")
        f = open(fi, 'r')
        print(f.read())
    except:
        print("FILE DOES NOT EXIT")

def write():
    try:
        fi = input("ENTER THE FILE NAME ")
        f = open(fi, 'w')
        d = input("ENTER DATA: ")
        f.write(d)
        f = open("k.txt", 'r')
        print(f.read())
    except:
        print("FILE DOES NOT EXIT")

def append():
        fi = input("ENTER THE FILE NAME ")
        f = open(fi, 'a+')
        d = input("ENTER DATA: ")
        f.write(" " +d)

def search():
    try:
        fi = input("ENTER THE FILE NAME ")
        f = open(fi, 'r')
        d = input("ENTER WORD TO SEARCH: ")
        c = f.read()
        if d in c:
            print("WORD IS FOUND")
        else:
            print("WORD IS NOT FOUND")
    except:
        print("FILE DOES NOT EXIT")
def delete():
    try:
        fi = input("ENTER THE FILE NAME ")
        import os
        os.remove(fi)
    except:
        print("FILE DOES NOT EXIT")
    else:
        print("FILE DELETED")

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
