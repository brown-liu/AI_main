import math









# use [ ] is a list / use () is called generator
x=[i for i in range(2000,3201) if i%7==0 and i%5!=0]
y=(i for i in range(2000,3201) if i%7==0 and i%5!=0)


#  * means all the elements inside that generator or list,  print can end with end= or sep=
print(*[i for i in range(2000,3201) if i%7==0 and i%5!=0],sep=',')


# list ()=[] dict() = {} OOP everthing is object
dict1={}
dict2=dict()
list1=[]
list2=list()


#list and dict comprehension
n=8
print({i:i**2 for i in range(1,n+1)})


# BE CAREFUL when rounding, DO not round the whole generator
print(*(round(math.sqrt(2*50*int(num)/30)) for num in list1),sep='-')


# BE CAREFUL when create lists in list, use .copy
# so those li_y inserted to li does not remain the same to each other.
li=[]
li_y=[]
for b in range(5):
    li.append(li_y.copy())

# sorted() return newlist sort work in line. abd key method in sort is useful, and BE CAREFULL lambda x: (must be a tuple)
word_in=[]
word_in.sort()
word_out=sorted(word_in)
word_out.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))

#yield can repeat, return only return once and stop

# def user_input():
#     while True:
#         s=input()
#         if not s:
#             return
#         yield s


#map(function,iterable)
def cal(x):
    return x+1111
# a=(x for x in range(5))
# x=map(cal,a)
# for i in x:
#     print(i)


# convert binary to int/decimal, can also convert from hex/oct
int('10100101',2)


#all return True if all True
all([True,True])     #  ==> True
all([True,True,False])# ==> False

#string methods
a='asdasd 1231'
a.isalpha()
a.isascii()
a.isdecimal()
a.isdigit()
a.islower()
a.isupper()
a.isnumeric()

# one example of using map and use many variable to receive multi args output
# in_word=input().split(' ')
# x,y =map(str,in_word)


#example of regular expression For password, A-Z a-z 0-9 include$#@
import re

ass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")

# max also have a key as function before comparision
# Note, map may return True or False while Filter act based on the condition
a=[1,2,3,5,6,7,9]
#input must be a list or iterable
li_map=map(lambda x:x>4,a)
# li_map=map(int,input("Enter number"))
print(list(li_map))
li_filter=filter(lambda x:x>4,a)
print(list(li_filter))
# ===> [False, False, False, True, True, True, True]
# ===> [5, 6, 7, 9]


#eval
# >>>x = 7
# >>> eval( '3 * x' )
# 21
# >>> eval('pow(2,2)')
# 4
# >>> eval('2 + 2')
# 4
# >>> n=81
# >>> eval("n + 4")
# 85


# random.random() give 0-1 float, random.uniform(start,end)
K=10
import random
random.random()
random.uniform(10,100)
random.sample(a,K) # to obtain K samples, the sample will not repeat, next sample will never be the same as current sample
random.choice()  # random choose one, next choice might be same as current choice
random.randrange(10,20)  # random choose one from the range
random.shuffle(a) # shuffle in line, return NONE

# import zlib as compression lib
import zlib
s="""K=10random.randrange(10,20)  # random choose one from the range"""
b=bytes(s,'utf-8')
print(b)
compressed=zlib.compress(b)
print(f'compressed {compressed}')
decompressed=zlib.decompress(compressed)
print(f'decompressed={decompressed}')

# itertools.product(a,b,c), make a generator/iterator which can provide the product of a and b and c
import itertools
a=[1,2,3]
b=[7,8,9]
c=[0,0,0]
d=[2,6,8]
itertools.product(a,b,c)
itertools.permutations(d)

# list compehension
nd_array=[[[0 for a in range(3)] for b in range(5)] for c in range(8)]
# (any can be i or can be anything,even a list) for item(or any name) in range(x)

# wrap
from textwrap import wrap
wrap('string',len('lengthperline'))

# use string.center(<length>,'replace Charactor')
# a='brown'
# >>> a.center(20,'*')
# '*******brown********'

# calinder

# import calendar
#
# year,month,day=map(int,input().split())
# dayId=calendar.weekday(year,month,day)
# print(calendar.day_name[dayId].upper())

a=1.232323232
print(f'{a:0.2f}')


import pickle
pickle.load()
pickle.dump()

#True False can also do operation
x=True+True
print(x)