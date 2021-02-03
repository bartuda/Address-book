#source https://www.youtube.com/watch?v=PxZE0e-ePoI&ab_channel=BeAPythonDev

class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        #print(self.first + " " + self.last)
        print(f'{self.first} {self.last}')

    def __str__(self):
        #return_string = "____________\n"       - line skip
        return f"{self.first} {self.last} : {self.age} : {self.phone_number}\n"

print("Welcome to the address book program")
print("Enter your contact's information")

first_name = input("First name = ")
last_name = input("Last name = ")
age =  input("Age = ")
phone_number = input("Phone number = ")

print(("Thank you"))

our_contact = Person(first_name, last_name, age, phone_number)
print(our_contact)