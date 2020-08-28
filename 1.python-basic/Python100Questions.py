
import time
import math

"""
Question 1
Question:
Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
"""



# for number in range(2000,3201):
#     if number %7==0 and number%5!=0:
#         print(number,end=',')
# print(*[i for i in range(2000,3201) if i%7==0 and i%5!=0],sep=',')
#
# x=[i for i in range(2000,3201) if i%7==0 and i%5!=0]
# y=(i for i in range(2000,3201) if i%7==0 and i%5!=0)
# print(type(x),type(y))

'''
Question 2
Question:
Write a program which can compute the factorial of a given numbers.The results should be 
printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''
# n= int(input('Please give a number'))
# result=1
# for i in range(n,0,-1):
#     result*=i
#
# print(result)

'''
Question 3
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
# n=int(input("Enter a number"))
# dict_result= {}
# for i in range(1,n+1):
#     dict_result[i]=i**2
# print(dict_result)
# n=8
# print({i:i**2 for i in range(1,n+1)})

'''Question 4
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a
list and a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''


# n=input("Enter Number")
# li=[]
# while n !='q':
#     li.append(n)
#     tuple1=tuple(li)
#     print(li)
#     print(tuple1)
#     n=input("Enter Number")

# print(tuple(input("Enter numbers separated by,").split(',')))
'''Question 5
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
# class Test:
#     def getString(self):
#         self.string=input("Please Enter a string")
#     def printString(self):
#         print(self.string.upper())
#     def test(self):
#         self.getString()
#         self.printString()
#
# test=Test()
# test.test()

'''
Question 6
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24'''

# nums=input("Enter numbers separeted by ',': ")
# list_num=nums.split(',')
# for num in list_num:
#     print(round(math.sqrt((2*50*int(num))/30)),end=',')
#
# print(*(round(math.sqrt(2*50*int(num)/30)) for num in list_num),sep='-')
'''Question 7
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
# x=3
# y=5
# li_y=[]
# for a in range(y):
#     li_y.append([])
# li=[]
# for b in range(x):
#     li.append(li_y.copy())
#
# for i in range(x):
#     for j in range(y):
#         li[i][j]=i*j
# print(li)

'''Question 8
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world'''

# word_in=['ccd','cds','bba','ax','ww','ac']
# word_out=sorted(word_in)
# print(*(x for x in word_out),sep=',')
#
# word_in=['ccd','cds','bba','ax','ww','ac']
# word_in.sort()
# print(*(x for x in word_in))

'''Question 9
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''
# def user_input():
#     while True:
#         s=input()
#         if not s:
#             return
#         yield s
# for line in map(str.upper,user_input()):
#     print(line)

'''Question 10
Question
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
'''
# word_in=input("put all your words").split(' ')
# new_li=[]
# for word in word_in:
#     if word in new_li:
#         continue
#     else:
#         new_li.append(word)
# new_li.sort()
# print(*(w for w in new_li),sep='^')
#
'''Question 11
Question
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
'''
# def bin_dec(binary_):
#     sum=0
#     binary_=str(binary_)[::-1]
#     for i in range(len(binary_)):
#         str_bin=binary_[i]
#         n= int(str_bin) * pow(2,i)
#         sum+=n
#     return sum

# b_in = input('bring binary').split(',')
#
# li=[]
# for b in b_in:
#     # if bin_dec(b)%5 ==0:
#     if int(b,2)%5==0:
#         li.append(b)
# print(li)

'''Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such 
that each digit of the number is an even number.The numbers obtained should be printed in a
comma-separated sequence on a single line.'''

# def even_num(in_num):
#     for i in str(in_num):
#         if int(i)%2!=0:
#             return False
#     return True
#
#
# for num in range(1000,3001):
#     if even_num(num):
#         print(num,end=',')


'''Question 13
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3'''

# mix='hello world! 123'
# letter_count=0
# digit_count=0
# for i in mix:
#     if i.isalpha():
#         letter_count+=1
#     if i.isdigit():
#         digit_count+=1
#
# print(f'LETTER {letter_count }\nDIGITS {digit_count}')


'''Question 14
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9'''
#
# a='Hello world!'
# print(a[0].isupper(),a[3].islower())
#


'''Question 15
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106'''

# n=9
#
# result=9+99+999+9999
# li=[]
# sum=0
#
# for i in range(1,5):
#     string = ''
#     for j in range(i):
#         string+=str(n)
#         print(string)
#     sum+=int(string)
# print(sum)

'''Question 16
Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
>Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81'''
# num_in=input('numbers').split(',')
# print(*(int(i)*int(i) for i in num_in if int(i)%2==0),sep=',')
#


'''Question 17
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

# 500'''
# sum_list=[]
# while True:
#     command=input('enter').split(' ')
#     print(command)
#
#     if command[0]=='D':
#         sum_list.append(int(command[1]))
#     if command[0]=='W':
#         sum_list.append(-int(command[1]))
#
#     print(sum(sum_list))

# in_word=input().split(' ')
# x,y =map(str,in_word)
#
# print(x+y)


'''Question 18
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1'''

# import re
# while True:
#     in_word=input('please enter password')
#     pattern=re.compile(r'[A-Za-z0-9$#Q]')
#     if re.match(pattern,in_word) and 12> len(in_word)>6:
#         print(in_word)


'''Question 19
Question:
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, 
age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]'''

# data_list = []
# while True:
#     data_in=tuple(input('Please enter Name, age and score').split(','))
#     if len(data_list)!=0:
#         data_list.append(data_in)
#         data_list.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))
#
#     else:
#         data_list.append(data_in)
#     print(data_list)



'''Question 20
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
'''
# class Divisable:
#     @staticmethod
#     def func1(num):
#         for i in range(1,num+1):
#             if num%i==0:
#                 yield i
#
# for i in Divisable.func1(7):
#     print(i)

'''Question 21
Question:
A robot moves in a plane starting from the original point (0,0).
 The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
 The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
 Please write a program to compute the distance from current position after a sequence of
 movement and original point. If the distance is a float, then just print the nearest integer. 
 Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2'''
# class Game:
#     x_axis=[]
#     y_axis=[]
#     x_locatiopn=0
#     y_location=0
#     def start(self):
#         command=tuple(input('input direction followed by number of steps:\n').split(' '))
#         self.calc_distance(command)
#         self.x_location=sum(self.x_axis)
#         self.y_location=sum(self.y_axis)
#
#         return math.sqrt(pow(self.x_location,2)+pow(self.y_location,2))
#
#     def calc_distance(self,command):
#         if command[0].upper()=='UP':
#             self.y_axis.append(int(command[1]))
#         if command[0].upper() == 'DOWN':
#             self.y_axis.append(-int(command[1]))
#
#         if command[0].upper() == 'LEFT':
#             self.x_axis.append(-int(command[1]))
#         if command[0].upper() == 'RIGHT':
#             self.x_axis.append(int(command[1]))
#
# game=Game()
# while True:
#     print(f'Distance = {game.start()}')
#     print(f'Current Location x = {game.x_location}\ny= {game.y_location}')
#

'''Question 22
Question:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''
# import collections
#
# in_word=input('Input phrase').split(' ')
# li_count=collections.Counter(in_word).items()
# li_count=list(li_count)
# print(li_count)
# li_count.sort()
# print(li_count)

'''Question 23
Question:
Write a method which can calculate square value of number'''

# def method1(num):
#     return num**2
# def method2(num):
#     return pow(num,2)
# def method3(num):
#     return num*num



'''Question 24
Question:
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

Hints:'''

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# def method3(num):
#     '''Take a number and return square of this number'''
#     return num*num
# print(method3.__doc__)

'''Question 25
Question:
Define a class, which have a class parameter and have a same instance parameter.
Question 26
Question:
Define a function which can compute the sum of two numbers.
Question 27
Question:
Define a function that can convert a integer into a string and print it in console.
Question 28
Question:
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
Question 29
Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.
Question 30
Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
Question 31
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Question 32
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the keys only.
Question 33
Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Question 34
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.
Question 35
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.
Question 36
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
Question 37
Question:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

Question 38
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
'''
tuple1=(1,2,3,4,5,6,7,8,9,10)
for idx,number in enumerate(tuple1):
    if idx<(len(tuple1)//2):
        print(number,end='')
    elif idx==(len(tuple1)//2):
        print(f'\n{number}',end='')
    else:

        print(number,end='')



