
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
# tuple1=(1,2,3,4,5,6,7,8,9,10)
# for idx,number in enumerate(tuple1):
#     if idx<(len(tuple1)//2):
#         print(number,end='')
#     elif idx==(len(tuple1)//2):
#         print(f'\n{number}',end='')
#     else:
#
#         print(number,end='')


'''Question 39
Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
Question 40
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".'''
#
# while True:
#     in_word=input('yes?').strip()
#     if in_word.lower()=='yes':
#         print("Yes")
#     else:print('No')

'''Question 41
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:
Question 42
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

'''
    # def square(x):
    #     return pow(x,2)
    # def even(x):
    #     if x%2==0:
    #         return x
    # a=[1,2,3,4,5,6,7,8,9]
    # li=map(lambda x:x>5,a)
    # print('Using Map',li,type(li))
    # li1=filter(lambda x:x>5,a)
    # print('Using Filter',li1,type(li1))
    # print(list(li),'-',list(li1))
    #

'''Question 43
Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

'''
#
# result=filter(lambda x: x%2!=0,range(1,21))
# print(list(result))


'''Question 44
Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).'''
# print(list(map(lambda x:x**2,range(1,21))))

'''Question 45
Question:
Define a class named American which has a static method called printNationality.
Question 46
Question:
Define a class named American and its subclass NewYorker.
'''
# class American:
#     def IsStupid(self):
#         print("Not all American are stupid")
# class NewYork(American):
#     pass
# nyc=NewYork()
# nyc.IsStupid()


'''Question 47
Question
Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.'''

# class Circule:
#     def __init__(self,radius):
#         self.radius=radius
#     def find_area(self):
#         return math.pi*(self.radius*self.radius)
# circule=Circule(10)
# print(circule.find_area())


'''Question 48
Question
Define a class named Rectangle which can be constructed by a length and width.   The Rectangle class has a method which can compute the area.
Question 49
Question
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Question 50
Question
Please raise a RuntimeError exception.
'''
# raise RuntimeError('Allgood')

'''Question 51
Question
Write a function to compute 5/0 and use try/except to catch the exceptions.

'''
# try:
#     x=5/0
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print('So stupid')


'''Question 52
Question
Define a custom exception class which takes a string message as attribute.

'''
#
# class Errors_1(Exception):
#     """My own exception class
#
#        Attributes:
#            msg  -- explanation of the error
#        """
#     def __init__(self,msg):
#         self.msg=msg
#
# try:
#     n=1/0
#
# except:
#     raise Errors_1('RHI ADAFASFASFA S')

'''Question 53
Question
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
In case of input data being supplied to the question, it should be assumed to be a console input.

# '''
# import re
# emai=input('Please enter email address')
# pattern=re.compile(r'[a-zA-Z]*@')
# name=re.match(pattern,emai)
#
# print(name.group()[:-1])

# email=input('enter email addres: ').split('@')
# print(email[0])
#
# import re
#
# email = "john@google.com elise@python.com"
# pattern = "(\w+)@\w+.com"
# ans = re.findall(pattern,email)
# print(ans)
#




'''Question 54
Question
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

# email=input('EMAIL AADREES').split('@')
# email=email[1].split('.')
# email=email[0]
# print(email)


'''Question 55
Question
Write a program which accepts a sequence of words separated by 
whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']'''

# phrase=input('Enter phrase').split(' ')
# li=[]
# for i in phrase:
#     if i.isdigit():
#         li.append(i)
#
# print(li)
# import re
# phrase=input('Enter phrase')
# pattern=re.compile('\d+')
# string=re.findall(pattern,phrase)
# print(string)


'''Question 56
Question
Print a unicode string "hello world".'''
# u=b'hello world'
# print(u)


'''Question 57
Question
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

'''
# def AscII2unicode(ascII):
#     result=''
#     for i in ascII:
#         result+=str(ord(i))
#     return result
#
# print(AscII2unicode('abbc'))


'''Question 58
Question
Write a special comment to indicate a Python source code file is in unicode.
Question 59
Question
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5
Then, the output of the program should be:

3.55'''
# def iter_divide(n):
#     a=1
#     sum=0
#     while a<=n:
#         sum+=a/(a+1.0)
#         a+=1
#     return sum
# print(round(iter_divide(5),2))


'''Question 60
Question
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).

Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# num=int(input('Number'))
# def func(num):
#     if num>0:
#         return func(num-1)+100
#     return 0
# print(func(num))


'''Question 61
Question
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7
Then, the output of the program should be:

13'''

# def Fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(7))




'''Question 62
Question
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7
Then, the output of the program should be:

0,1,1,2,3,5,8,13
In case of input data being supplied to the question, it should be assumed to be a console input.'''

# def Fibonacci(n):
#     if n==0:
#         return 0
#
#     elif n==1:
#         return 1
#
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# for i in range(8):
#     print(Fibonacci(i))


'''Question 63
Question
Please write a program using generator to print the even numbers between 0 and n in 
comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10
Then, the output of the program should be:

0,2,4,6,8,10'''
# n=int(input('number'))
# print(*(i for i in range(n+1) if i%2==0))

# def Generator(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i
# x=Generator(10)
# for i in range(3):
#     print(next(x))

'''Question 64
Question
Please write a program using generator to print the numbers
which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example: If the following n is given as input to the program:
100
Then, the output of the program should be:

0,35,70'''

# def Generator(num):
#     for n in range(num):
#         if all([n%5==0, n%7==0]):
#             print(n)
# print(Generator(100))


'''Question 65
Question
Please write assert statements to verify that every number in the list [2,4,6,8] is even.'''
#
# for i in [2,4,6,8]:
#     assert i%2==0



'''Question 66
Question
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:
38'''

# calc=input('enter calculation')
# print(eval(calc))

'''Question 67
Question
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.

'''
# a=[1,4,5,6,7,8,9,10,12,15,19,20,22,23,26,27,29]
# target=26
# #index=4
#
# def binary_search(a,target):
#     low=0
#     hi=len(a)
#     mid = (low + hi) // 2
#     while a[mid]!=target:
#         mid = (low + hi) // 2
#         if a[mid]>target:
#             hi=mid
#         elif a[mid]==target:
#             return mid
#         else:
#             low=mid
#
#
# print(a.index(target))
# print(binary_search(a,target))

'''Question 68
Question
Please generate a random float where the value is between 10 and 100 using Python module.
'''
import random
# for i in range(5):
#     print(random.uniform(10,100))
#     print(random.random()*100)


'''Question 69
Question
Please generate a random float where the value is between 5 and 95 using Python module.
Question 70
Question
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
'''
# a=[2,5,6,8,3,4,5,6,8,10,2,3,44,332,21]
# li_even=[i for i in a if all([i %2==0,0<=i<=10])]
# print(li_even)

'''Question 71
Question
Please write a program to output a random number, which is divisible by 5 and 7, 
between 10 and 150 inclusive using random module and list comprehension.'''


# a=[i for i in range(10,151) if i%5==0 and i%7==0]
# rand=random.sample(a,1)
# choi=random.choice(a)
# print(f'random.sample=>>{rand}\nrandom.choice==>>{choi}')



'''Question 72
Question
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.'''

# a=[i for i in range(100,200)]
# choice=random.sample(a,5)
# print(choice)

'''Question 73
Question
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Question 74
Question
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
Question 75
Question
Please write a program to randomly print a integer number between 7 and 15 inclusive.
Question 76
Question
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''

# s="hello world!hello world!hello world!hello world!"
# b=bytes(s,'utf-8')
# print(b)
# import zlib
# compressed=zlib.compress(b)
# print(f'compressed {compressed}')
# decompressed=zlib.decompress(compressed)
# print(f'decompressed={decompressed}')

'''Question 77
Question
Please write a program to print the running time of execution of "1+1" for 100 times.
Question 78
Question
Please write a program to shuffle and print the list [3,6,7,8].'''


# x=[1,2,3,4,5,6,7,8]
# random.shuffle(x)
# print(x)

'''Question 79
Question
Please write a program to generate all sentences where subject is in ["I", "You"]
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''
a=["I", "You"]
b=["Play", "Love"]
c=["Hockey","Football"]

# for i in a:
#     for j in b:
#         for k in c:
#             print(f'{i} {j} {k}')

# import itertools
# x=itertools.product(a,b,c)
# for i in x:
#     print(i)


'''Question 80
Question
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

 '''
# a=[5,6,77,45,22,12,24]
# print([i for i in a if i %2!=0])

'''Question 81
Question
By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

'''
# list1=[12,24,35,70,88,120,155]
# list2=[x for x in list1 if x%5==0 and x%7==0]
# for x in list2:
#     print(x)


'''Question 82
Question
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].'''
# list1=[12,24,35,70,88,120,155]
# list2=[x for x in list1 if list1.index(x) not in [0,2,4,6]]
# print(list2)
# list2=[x for idx,x in enumerate(list1) if idx %2!=0]
# print(list2)

'''Question 83
Question
By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
Question 84
Question
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.'''
#
# nd_array=[[[0 for a in range(3)] for b in range(5)] for c in range(8)]
# print(nd_array)


'''Question 85
Question
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
Question 86
Question
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
Question 87
Question
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
'''
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
#
# li=set.intersection(set(list1),set(list2))


'''Question 88
Question
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
'''
a=[12,24,35,24,88,120,155,88,120,155]
# print(sorted(set(a),reverse=True))

'''Question 89
Question
Define a class Person and its two child classes: 
Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Question 90
Question
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1'''
# from collections import Counter
# def convert(string):
#     print(Counter(string).items())
#
# convert('abcdefgabc')


'''Question 91
Question
Please write a program which accepts a string from console and print it in reverse order.

Example: If the following string is given as input to the program:*

rise to vote sir
Then, the output of the program should be:

ris etov ot esir'''

# a='abcdefg'
# print(a[::-1])
# print(''.join(reversed(a)))


'''Question 92
Question
Please write a program which accepts a string from console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld'''

# a='H1e2l3l4o5w6o7r8l9d'
# b=''
# for i in a:
#     if i.isalpha():
#         b+=i
# print(b)


'''Question 93
Question
Please write a program which prints all permutations of [1,2,3]
'''
# import itertools
# a=[1,2,3]
# # for i in itertools.product(a,a,a):
# #     print(i)
# print(list(itertools.permutations(a)))


'''Question 94
Question
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 
legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
'''

# for rabit in range(35):
#     if rabit*4+(35-rabit)*2==94:
#         print(rabit)

'''Question 95
Question
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5
Then, the output of the program should be:

5'''
# x=[2,3,6,6,6,5,5,4]
# def find_run_up(result):
#     for _ in range(result.count(max(result))):
#         result.remove(max(result))
#     for _ in range(result.count(max(result))) :
#         print(max(result))
# find_run_up(x)


'''Question 96
Question
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''
from textwrap import wrap
string='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# print(string,4)




'''Question 97
Question
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------'''

# import string
#
# def print_rangoli(size):
#     n=size
#     alph=string.ascii_lowercase
#     width=4*n*3
#     ans=[]
#     for i in range(n):
#         right='-'.join(alph[n-i-1:n])
#         mid=right[-1:0:-1] +right
#         final=mid.center(width,'-')
#         ans.append(final)
#         print(final)
#     ans.pop()
#     for i in reversed(ans):
#         final2=i.center(width,'-')
#         print(final2)
#
# print_rangoli(3)
# import string
# def run(n):
#     alpha=string.ascii_lowercase
#     width=n*2+4
#     answer=[]
#     for idx in range(n):
#         right=alpha[n-idx-1:n]
#         mid= right[-1:0:-1] + right
#         final=mid.center(width,'*')
#         print(final)
#
# run(5)


'''Question 98
Question
You are given a date. Your task is to find what the day is on that date.

Input

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

08 05 2015
Output

Output the correct day in capital letters.

WEDNESDAY'''

# import calendar
#
# year,month,day=map(int,input().split())
# dayId=calendar.weekday(year,month,day)
# print(calendar.day_name[dayId].upper())


'''Question 99
Question
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input

The first line of input contains an integer, M.The second line contains M space-separated integers.
The third line contains an integer, N.The fourth line contains N space-separated integers.

4
2 4 5 9
4
2 4 11 12
Output

Output the symmetric difference integers in ascending order, one per line.

5
9
11
12
'''
# if __name__ == '__main__':
#     n = int(input())
#     set1 = set(map(int,input().split()))
#
#     m = int(input())
#     set2 = set(map(int, input().split()))
#
#     ans = list(set1 ^ set2)
#     ans.sort()
#     for i in ans:
#         print(i)


'''Question 100
Question
You are given words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:

3
2 1 1
Question 101
Question
You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1
'''

# string=','.join(input('input string'))
# string=string.split(',')
# dict1={}
# for i in string:
#     if i not in dict1.keys():
#         dict1[i]=1
#     else:
#         dict1[i]+=1
# print(dict1)
# for i in dict1:
#     print(i,dict1[i])


'''Question 102
Question
Write a Python program that accepts a string and calculate the number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8'''

# word=input()
# digit,alpha=0,0
#
# for char in word:
#     digit+=char.isdigit()
#     alpha+=char.isalpha()
# print(f'digit{digit}')
# print(f'alpha{alpha}')


'''Question 103
Question
Given a number N.Find Sum of 1 to N Using Recursion

Input

5
Output

15'''
# def add(num):
#     if num>0:
#         return num+add(num-1)
#     else:
#         return 0
#
# print(add(5))