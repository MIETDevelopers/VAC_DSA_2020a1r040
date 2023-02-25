

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
