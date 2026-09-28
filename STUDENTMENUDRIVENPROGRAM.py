# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student():
    def _init_(self):
        self.rollno=int(input("enter rollno:"))
        self.name=input("enter name")
        self.mark=int(input("enter mark"))

    def updatemark(self):
        self.mark=int(input("enter mark"))


    def display(self):
        print(l)
l=[]
while(1):
    print("1.Add Student(roll no,name,marks)")
    print("2.Update Marks")
    print("3.Display All Student Details")
    print("4.Search Student by Roll Number")
    print("5.Delete Student")
    print("6.exit")

    ch = int(input("enter your choice:"))

    if ch==1:
        s=Student()
        l.append(s)
        print(l)
    elif ch==2:
        n=int(input("enter the rollno"))
        for i in l:
            if i.rollno==n:
                i.updatemark()
                break
        else:
            print("roll no doesnt exit")


    elif ch==3:
        for i in l:
            i.display()


    elif ch==4:
        n = int(input("enter the rollno"))
        for i in l:
            if i.rollno == n:
                print("student found")
                break
        else:
            print("roll no doesnt exit")


    elif ch==5:
        n = int(input("enter the rollno"))
        for i in l:
            if i.rollno == n:
                i.remove(i)
                break
        else:
            print("roll no doesnt exit")

    else:
        exit()

