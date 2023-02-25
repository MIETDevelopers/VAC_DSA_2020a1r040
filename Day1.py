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

