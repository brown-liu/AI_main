import numpy as np
'''
1. Import the numpy package under the name np (★☆☆)
2. Print the numpy version and the configuration (★☆☆)
3. Create a null vector of size 10 (★☆☆)
4. How to find the memory size of any array (★☆☆)
'''
print(np.__version__)
print(np.__config__)
# print(np.show_config())
vector_10=np.zeros(10)
print(vector_10,vector_10.size * vector_10.itemsize )
print(f'size of each item in array is {vector_10.itemsize} bytes')

'''
6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
7. Create a vector with values ranging from 10 to 49 (★☆☆)
8. Reverse a vector (first element becomes last) (★☆☆)
9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
'''
array=np.zeros(10)
array[4]=1
print(array)

array=np.arange(10,49)
print(array,len(array))

array=np.arange(1,10)
print(array[::-1])
array=np.arange(9,0,-1)
print(array)

array_3x3=np.arange(9).reshape((3,3))
print(array_3x3)

a=[1,2,0,0,4,0]
zero=np.nonzero(a)
print(zero)

'''
11. Create a 3x3 identity matrix (★☆☆)
12. Create a 3x3x3 array with random values (★☆☆)
13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
14. Create a random vector of size 30 and find the mean value (★☆☆)
15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
'''
# ide=np.eye(3)
# print(ide)
#
# rand=np.random.random((3,3,3))
# print(rand)

# array_10x10=np.random.random((10,10))
# print(array_10x10)
# print(np.argmax(array_10x10),np.max(array_10x10))
# print(array_10x10.min())

# vec=np.random.random(10)
# print(vec,np.mean(vec))

# array=np.ones((5,5))
# array[1:-1,1:-1]=0
# print(array)

'''16. How to add a border (filled with 0's) around an existing array? (★☆☆)'''
# array=np.ones((10,10))
# array=np.pad(array,pad_width=1,mode='constant')
# print(array)


'''
17. What is the result of the following expression? (★☆☆)
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1
'''
# a=3
# b=3*1
# c=0.3
# d=0.3*1
# print(a == b)  >True
# print(c == d)   > False

'''18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)

diag(v, k=0)
    Extract a diagonal or construct a diagonal array.

Parameters
    ----------
    v : array_like
        If `v` is a 2-D array, return a copy of its `k`-th diagonal.
        If `v` is a 1-D array, return a 2-D array with `v` on the `k`-th
        diagonal.
    k : int, optional
        Diagonal in question. The default is 0. Use `k>0` for diagonals
        above the main diagonal, and `k<0` for diagonals below the main
        diagonal.

'''

# arr=np.diag(1+np.arange(4),k=-1)
# print(arr)

'''19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)'''


# z=np.zeros((8,8))
# z[1::2,1::2]=1
# z[::2,::2]=1
# # z[1::2,-1]=1
# print(z)

'''20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?'''
# array=np.array(range(6*7)).reshape((7,6))
# print(array)
# print(np.unravel_index(indices=[22,41,37],shape=(7,6)))

'''[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]]
(array([3, 6, 6], dtype=int64), array([4, 5, 1], dtype=int64))'''

'''21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)'''

# sum(iterable,startwith)   sum(range(5),-1) =>> 0+1+2+3+4 + -1 = 9
#different between python sum and numpy sum
import numpy as np
a=np.sum(range(5),-1)
b=sum(range(5),-1)
print(f"np.sum(iterator,axis can only be axis number ==>a=np.sum(range(5),-1) ==>){a}")
print("standard sum(iterator,startfrom) ===>",b)
print("\n HOw to print yesterday and tomorrow date?\n")
yesterday = np.datetime64('today','D') - np.timedelta64(1,'D')
print(f"np.datetime64(1,'D')===>{np.datetime64(1,'D')}")
print(f"np.timedelta64(1,'D')",np.timedelta64(1,'D'))
print(f"yesterday = np.datetime64('today','D') -np.datetime64(1,'D')=>>>",yesterday)
print(f"tomorrow = np.datetime64('today','D')==>{np.datetime64('today','D')}")
# print(f"tomorrow =np.datetime64('today','d') + np.timedelta64(1,'d')",np.datetime64('today','D')+np.timedelta(1,'D'))
print("*".center(40,"*"))
print("print all date in that month")
dates=np.arange('2016-07','2016-09',dtype='datetime64[D]')
print(dates)
print("*".center(40,"*"))
a=np.ones(3)
b=np.random.randn(3)
c=np.zeros(3)
print(a,'\n',b,"\n",c,"\n")
print(f"This is inplace a+b =>> {np.add(a,b,out=b)}")   # out = b means the new value will overwrite b
print(f"This is inplace a*b =>> {np.multiply(a,b,out=b)}")
print(f'This is inplace subtract =>>> {np.subtract(a,c,out=b)}')
print(f'This is inplace divide ===> {np.divide(a,b,out=b) }')
print(f"a{a}")
print(f"{b}")
##get a random array
print(np.random.randn(2,2))
random_array = np.random.uniform(0,10,10)
print(random_array)
print(np.floor(random_array))
print(np.ceil(random_array)-1)
print(random_array.astype(int))
print(np.trunc(random_array))

print("*".center(50,"V"))
#create a 5x5 matrix and add vector so it apply to all lines
a=np.zeros((5,5))
b=np.arange(0,5)
print(a+b)

def gntr():
    for x in range(10):
        yield x
x=np.fromiter(gntr(),dtype=float,count=-1)
print(x)

#check if two matrix /array is the same
np.allclose(a,b)
np.array_equal(a,b)

# read only
Z=np.array(10)
Z.flags.writable=False