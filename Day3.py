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
