#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:19:56 2018

@author: Anastasia
"""

#%% ex.1 



#Create a Student class that has the following attributes:


# name
#last name
   # age
    #master (either MCSBT or MDBI)

 #Make sure you parametrize all those fields in the constructor.
 
class Student:
    def __init__ (self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master 

Anastasia = Student("Anastasia", "Lasunina", "25", "MDBI")




#%% ex. 2 

#Add a print_student method in the Student class that prints a line 
#like follows for the object
#Pepe García is a 55 year old student of the MCSDBI masters programme
#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call print_student on each one to print its description.

class Student:
    def __init__ (self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master 
    
    def print_student(self):
        print(self.name + " " + self.last_name + " is a " + self.age + " year old student of the " + self.master +" masters programm")
        
students = [
Student("Arthur", "Maroquene-Froissart", '23' , "MCSBT")
,Student( "Alejandro", "Meneses", "27", "MCSBT")
,Student("Agata", "Kaczmarek", "31","MDBI")
,Student("Anastasia", "Lasunina", "25", "MDBI")
,Student("Anikken", "Barstad Gjeruldsen", "27", "MDBI")
,Student("Candela", "Noya", "24", "MDBI")
,Student("Daniil", "Osipov", "21", "MDBI")
,Student("David", "Barrero Gonzalez", "31", "MCSBT")
,Student("Edem", "Francois", "28", "MCSBT")
,Student("Eduardo", "Paraja", "23", "MDBI")
,Student("Felix ", "Fastrich", "23", "MDBI")
,Student("Florian", "Diegruber", "25", "MCSBT")
,Student("Hannah", "Oldorf", "23", "MCBT")
,Student("Isabella", "Rosenthal", "27", "MDBI")
,Student("Javier", "Fernandez", "24", "MCSBT")
,Student("Julie", "De Neys", "23", "MDBI")
,Student("Lukas", "Hauser", "28","MDBI")
,Student("Leila", "Tazi", "27", "MCSBT")
,Student("Laura", "Kageneck", "23", "MCSBT")
,Student("Marius", "Diedrich", "23", "MDBI")
,Student("Monica", "Alvarenga","28", "MDBI")
,Student("Natalie", "Cedeno", "26", "MDBI")
,Student("Octavio", "Ramírez", "28", "MDBI")
,Student("Tancredi", "Bernard", "21", "MCSBT")
,Student("Yasmine", "Lyagoubi", "23", "MDBI"),
Student("Zineb ", "Mezzour","22","MCSBT")
]

def show_students():  
    for student in students:
        student.print_student()
    

#%% ex. 3
        
#Migrate the music store program we created to an OOP approach.  
#You can use classes for modelling products, services, customer tier, the shopping cart...

#Products have name and price.
#Services have price.
#Customer tier have a discount.
#Shopping cart has:
# a list of product
# a list of services
# and a method to add new products and another for services
# a checkout method that receives a customer tier and calculates the price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
        

class Service:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 

class Customer:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount
productlist = []  
guitar = Product("guitar", 1000)
pick_box = Product("pick box", 5)
guitar_string = Product("guitar string", 10)

servicelist = []
insurance = Service("insurance", 5)
priority_mail = Service("priority mail", 10)

customer = ["gold", "silver", "normal"]

gold = Customer("gold", .95)
silver = Customer("silver", .98)
normal = Customer("normal", 1)
final_price1 = 0 

class Shopping_cart:
    def __init__(self, productlist, servicelist):
        self.productlist = productlist
        self.servicelist = servicelist
        
    def add_products(self, product):
            self.product.append(productlist)
            
    def add_services(self, service):
            self.service.append(servicelist)
        
    def checkout(self, customer):
            self.customer.price
        
for product in productlist:
    if customer == gold or silver:
        final_price1 += product.price * customer.discount
    else: 
        final_price1 += product.price 
                
            
            























