# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student:
    def _init_(self):
        print("Enter the details")
        self.roll = int(input("Enter Student roll no: "))
        self.name = input("Enter Student name: ")
        self.mark = int(input("Enter mark: "))
    def updateMark(self):
        new_mark = int(input("Enter new mark: "))
        self.mark = new_mark
        print("New mark updated successfully")
    def display(self):
        print("Roll No:",self.roll)
        print("Name:",self.name)
        print("Total Marks:",self.mark)


l = []

while(1):
    choice = int(input("1. Add Student\n2. Update Marks\n3. Display All Student Details\n4. Search Student by Roll Number\n5. Delete Student\n6. Exit\nEnter your choice: "))
    if choice == 1:
        s = Student()
        l.append((s))
        print("New Student Added Successfully.")
    elif choice == 2:
        number = int(input("Enter roll number: "))
        for i in l:
            if i.roll == number:
                i.updateMark()
                break
        else:
            print("Student doesn't exist")
    elif choice == 3:
        for i in l:
            i.display()


    elif choice == 4:
        target = int(input("Enter roll number: "))
        for i in l:
            if i.roll == target:
                print("Found Student")
                break

        else:
            print("Student doesn't exist")
    elif choice == 5:
        number = int(input("Enter roll number: "))
        for i in l:
            if i.roll == number:
                l.remove(i)
                print("Removed")
                break

        else:
            print("Student doesn't exist")
    elif choice == 6:
        exit()
    else:
        print("Invalid Choice!")