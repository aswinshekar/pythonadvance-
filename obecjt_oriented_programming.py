from typing import cast


# _____________________________________________________________________INHERITANCE______________________________________________________________________________________________________________________________


# class Parent:
#     def m1(self):
#         print("FUNCTION OF CLASS PARENT M1")
#     def m2(self):
#         print("FUNCTION OF CLASS PARENT M2")
#
# class Child(Parent):
#     j=3
#     def m1(self):
#         if self.j ==1:
#              super().m1()
#         else:
#             print("FUNCTION OF CHILD CLASS M1 (METHOD OVERRIDING)")
# c=Child()
# c.m1()
# c.m2()


# 2
#
# class Person:
#     def __init__(self):
#         self.name=input("ENTER THE NAME: ")
#         self.age=int(input("ENTER THE AGE :"))
#     def show(self):
#         print("NAME: ",self.name,"\nAGE: ",self.age)
# p=Person()
# p.show()
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rolno=input("ENTER THE ROLL NO: ")
#         self.mark=int(input("ENTER THE MARK :"))
#
#     def updatemark(self):
#             self.mark = int(input("ENTER THE UPDATED MARK"))
#     def show(self):
#         super().show()
#         print("ROLL NO: ",self.rolno,"\nMARK: ",self.mark)
#         # self.updatemark()
#     def updatemark(self):
#         self.mark=int(input("ENTER THE UPDATED MARK"))
#         self.show()
#
#
# c=Student()
# c.show()

# class Category:
#     def __init__(self):
#         self.category_name=input("ENTER CATEGORY NAME: ")
#     def show(self):
#         print("CATEGORY NAME: ",self.category_name)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.price=int(input("ENTER PRICE: "))
#         self.quantity = int(input("ENTER QUANTITY: "))
#     def total_price(self):
#         print("TOTAL PRICE: ",self.price * self.quantity)
# p=Product()
# p.show()
# p.total_price()

# class Company:
#     def __init__(self):
#         self.company_name=input("ENTER COMPANY NAME: ")
#         self.location=input("ENTER LOCATION: ")
#     def display_company(self):
#         print("COMPANY: ",self.company_name,"\nLOCATION: ",self.location)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.emp=input("ENTER EMPLOYEE NAME: ")
#         self.salary=int(input("ENTER EMPLOYEE SALARY: "))
#     def display_details(self):
#         self.display_company()
#         print("EMPLOYEE NAME: ",self.emp,"\nSALARY: ",int(self.salary))
#     def update_salary(self):
#         self.salary=self.salary+(self.salary * 10 / 100)
#         print(" ")
#         print("DETAILS AFTER SALARY INCREMENTED ")
#         self.display_details()
# c=Employee()
# c.display_details()
# c.update_salary()


# ________________________________________________________________________MULTIPLE LEVEL INHERITANCE________________________________




# class Hospital:
#     def __init__(self):
#         self.hos_name=input("ENTER HOSPITAL NAME: ")
#         self.location=input("ENTER LOCATION: ")
#         self.phone=int(input("ENTER PHONE NUMBER: "))
#     def display_hospital(self):
#         print("HOSPITAL NAME: ",self.hos_name,"LOCATION: ",self.location,"PHONE NUMBER: ",self.phone)
# class Department:
#     def __init__(self):
#         self.dept_name = input("ENTER DEPARTMENT NAME: ")
#         self.doctor_name= input("ENTER DOCTOR NAME: ")
#     def display_department(self):
#         print("DEPARTMENT NAME: ", self.dept_name, "\nDOCTOR NAME: ", self.doctor_name)
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name = input("ENTER PATIENT NAME: ")
#         self.age = input("ENTER AGE: ")
#         self.gender = input("ENTER GENDER: ")
#         self.phone = int(input("ENTER PHONE NUMBER: "))
#         self.admission_date = input("ENTER ADMISSION DATE: ")
#         self.bed_no = input("ENTER BED_NO: ")
#         self.discharge_date = input("ENTER DISCHARGE DATE: ")
#     def set_discharge(self):
#         self.discharge_date = int(input("UPDATE DISCHARGE DATE: "))
#         self.full_summary()
#     def full_summary(self):
#         Hospital.display_hospital(self)
#         Department.display_department(self)
#         print("PATIENT NAME: ",self.patient_name,"\nAGE: ",self.age,"\nGENDER: ",self.gender,
#               "\nPHONE NUMBER: ",self.phone ,
#              "\nADMISSION DATE: ",self.admission_date ,"\nBED_NO: ",self.bed_no)
#         if self.discharge_date ==" ":
#             print("NOT YET DISCHARGE")
#         else:
#             print("DISCHARGE DATE: ",self.discharge_date)
# c=Patient()
# c.full_summary()
# c.set_discharge()

#________________________________________________________________________________POLYMORPHISM______________________________

# ________________________________________________________________________________ABSTRACTION_____________________________
# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def get_area(self):
#         self.l=int(input("ENTER THE LENGHTH: "))
#         self.b=int(input("ENTER THE BREADTH: "))
#         print("AREA: ",self.l*self.b)
#     def get_perimeter(self):
#         print("PERIMETER: ",2*(self.l+self.b))
#
# class Square(Shape):
#     def get_area(self):
#         self.l=int(input("ENTER THE LENGHTH: "))
#         print("AREA: ",self.l*self.l)
#     def get_perimeter(self):
#         print("PERIMETER: ",4*self.l)
#
# s=Rectangle()
# s.get_area()
# s.get_perimeter()
# p=Square()
# p.get_area()
# p.get_perimeter()

#
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     def __init__(self):
#         self.empid=input("ENTER EMPLOYEE ID: ")
#         self.name=input("ENTER EMPLOYEE NAME: ")
#         self.age=int(input("ENTER EMPLOYEE AGE: "))
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class Full_time_employee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.sal=int(input("ENTER THE SALARY : "))
#     def calculate_salary(self):
#         print("FULL__TIME__EMPLOYEE\n")
#         print("EMPLOYEE ID: ",self.empid,"\nEMPLOYEE NAME: ",self.name,"\nEMPLOYEE AGE: ",self.age,"\nSALARY: ",self.sal)
# class Part_time_employee(Employee):
#     def __init__(self):
#         self.hour=int(input("ENTER THE HOUR: "))
#         self.rate=int(input("ENTER RATE/HOUR: "))
#     def calculate_salary(self):
#         print("PART__TIME__EMPLOYEE\n")
#         print("EMPLOYEE ID: ", self.empid, "\nEMPLOYEE NAME: ", self.name, "\nEMPLOYEE AGE: ", self.age, "\nSALARY: ",
#               self.hour*self.rate)
# f=Full_time_employee()
# f.calculate_salary()
# p=Part_time_employee()
# p.calculate_salary()









