

import numpy as np

# slicing with interval############################      array[   start  stop   step   interval ]

x = np.array([2,5,1,9,0,3,8,11,-4,-3,-8,6,10])
print(x[2::3])
# 2 is start index
# 3 is interval
print(x[2:-1:3])

##############################np.unravel_index(indices=[22,41,37],shape=(10,10))

#10 x 10 array, check number(3 and 5 and 12)'s location
#return 1st dim location and 2nd dim location and 3rd.....
# number 22 is in 3rd row , column 4
# number 41 is in 6th row , column 5
# number 37 is in 6th row , column 1

'''[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]]
(array([3, 6, 6], dtype=int64), array([4, 5, 1], dtype=int64))'''

# 创建全空数组，其实每个值都是接近于零的数
a = np.empty((3,4))
print(a)
# 创建连续数组
a = np.arange(10,21,2) # 10-20的数据，步长为2
print(a)
# 创建线段型数据
a = np.linspace(1,10,20) # 开始端1，结束端10，且分割成20个数据，生成线段
# 包含 start 和 end
print(a)
# Numpy中具有很多的数学函数工具
c = np.sin(a)
print(c)
# 多维度矩阵乘法  Do not use * for matrix
# 第一种乘法方式:
b=np.array([3,4,5])
c = a.dot(b)
print(c)
# 第二种乘法:
c = np.dot(a,b)
print(c)

#当axis的值为0的时候，(Column)将会以列作为查找单元，
#当axis的值为1的时候，(Row)将会以行作为查找单元。
# >>>a
#   array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14],
#        [15, 16, 17, 18, 19]])
# >>>sum(a)
#   array([30, 34, 38, 42, 46])
# >>>np.sum(a)
#   190
# >>>np.sum(a,axis=0)
#   array([30, 34, 38, 42, 46])
# >>>np.sum(a,axis=1)
#   array([10, 35, 60, 85])


# 累加
print(np.cumsum(a))

# 累差运算
B = np.array([[3,5,9],
              [4,8,10]])

# 后一个减去前一个 就等到diff
print(np.diff(B))

# np.nonzero(array) return 2 list contains indices on each axis where element is not 0
# start from row and then column

#np.clip(array, Array_min,Array_max)
# intake array, replace any element smaller than Array_min to Array_min, same to Array_max

A = np.arange(3,15).reshape((3,4))
####################################### flatten()
print(A.flatten())

#切片 b[(0,1,2,3,4),(1,2,3,4,5)]  get (0,1) (1,2) (2,3)......  == np.diag(b,k=1)

###############################################vstack((a,b)) hstack((a,b))

## convert list/array to matrix
A=np.array([1,2,3,4])
print(A.shape)
B=A[np.newaxis,:]
print(B,B.shape)

C=np.concatenate((A,B),axis=1)
D=np.concatenate((A,B),axis=0)

np.split(A,3)  #=>

print(np.vsplit(A,3)) # 等价于print(np.split(A,3,axis=0))
print(np.hsplit(A,2)) # 等价于print(np.split(A,2,axis=1))

# use .copy to copy value, = is poinitng at same memory address
np.bincount(a)
# b=np.array([0,4,5,5,5,7,9,10])
# np.bincount(b)
# Out[24]: array([1, 0, 0, 0, 1, 3, 0, 1, 0, 1, 1], dtype=int64)

np.round([1.1,2.2,3.3],0)

# np.where(x==1)
# Out[35]:
# (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64),
#  array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64))


