import numpy as np
'''
1. Import the numpy package under the name np (★☆☆)
2. Print the numpy version and the configuration (★☆☆)
3. Create a null vector of size 10 (★☆☆)
4. How to find the memory size of any array (★☆☆)
'''
# print(np.__version__)
# print(np.__config__)
# print(np.show_config())
# vector_10=np.zeros(10)
# print(vector_10,vector_10.size * vector_10.itemsize )
# print(f'size of each item in array is {vector_10.itemsize} bytes')

'''
6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
7. Create a vector with values ranging from 10 to 49 (★☆☆)
8. Reverse a vector (first element becomes last) (★☆☆)
9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
'''
# array=np.zeros(10)
# array[4]=1
# print(array)
#
# array=np.arange(10,49)
# print(array,len(array))
#
# array=np.arange(1,10)
# print(array[::-1])
# array=np.arange(9,0,-1)
# print(array)
#
# array_3x3=np.arange(9).reshape((3,3))
# print(array_3x3)
#
# a=[1,2,0,0,4,0]
# zero=np.nonzero(a)
# print(zero)

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

z=np.zeros((8,8))
z[1:2,:]=1
print(z)
