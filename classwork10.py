
# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie:
    def __init__(self):
        self.mvname=input("Enter Movie Name:")
        self.yr=int(input("Enter Year:"))
        self.lang=input("Enter Mv Language:")
        self.drctr=input("Enter Director:")
        self.rt=int(input("Enter Rating:"))

    def display_details(self):
        print("NAME OF MOVIE:",self.mvname)
        print("YEAR OF MOVIE:",self.yr)
        print("LANGUAGE OF MOVIE:",self.lang)
        print("DIRECTOR OF MOVIE:",self.drctr)
        print("RATING OF MOVIE:",self.rt)

    def update_rating(self):
        self.rt=int(input("Enter new rating:"))
        print("UPDATED RATING OF THE MOVIE:",self.rt)

m=Movie()
m.display_details()
m.update_rating()
m.display_details()

# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along
# with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.


class Vehicle:
    def _init_(self):
        self.brand = input("Enter Brand name:")
        self.model = input("Enter Model:")
        self.color = input("Enter Color:")
        self.year = int(input("Enter Year:"))


    def display(self):
        print("BRAND OF VEHICLE:", self.brand)
        print("MODEL OF VEHICLE:", self.model)
        print("COLOR OF VEHICLE:", self.color)
        print("YEAR OF VEHICLE:", self.year)
class Car(Vehicle):
    def _init_(self):
        super()._init_()
        self.mileage = int(input("Enter Mileage:"))

    def display(self):
        super().display()
        print("MILEAGE OF CAR:", self.mileage, "km/l")

class Bike(Vehicle):
    def _init_(self):
        super()._init_()
        self.cc = int(input("Enter CC:"))

    def display(self):
        super().display()
        print("CC OF BIKE:", self.cc)

c=Car()
c.display()
b=Bike()
b.display()
print("CAR DETAILS")
c = Car()
print("BIKE DETAILS")
b = Bike()
c.display()
b.display()