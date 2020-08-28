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

def user_input():
    while True:
        s=input()
        if not s:
            return
        yield s


#map(function,iterable)
def cal(x):
    return x+1111
a=(x for x in range(5))
x=map(cal,a)
for i in x:
    print(i)


# convert binary to int/decimal, can also convert from hex/oct
int('10100101',2)


#all return True if all True
all([True,True])
True
all([True,True,False])
False

#string methods
a='asdasd 1231'
a.isalpha()
a.isascii()
a.isdecimal()
a.isdigit()
a.islower()
a.isupper()
a.isnumerica()

# one example of using map and use many variable to receive multi args output
in_word=input().split(' ')
x,y =map(str,in_word)


#example of regular expression For password, A-Z a-z 0-9 include$#@
import re

ass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
