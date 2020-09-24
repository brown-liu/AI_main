np.zeros((row,column))
<hr>
np.arange(start,stop) =>create vector from start to stop with increament of 1. normally followed by .reshape(row,column) to redefine shape
<hr>
np.nonzero([1,2,3,4,5,0,0,0]) => return index of non-zero elements
<hr>
np.random.random((row,column))  => return row x column matrix with elements between 0-1,float64
<hr>   
np.random.randint(0,10,10) =>start from 0,end 9,having 10 elements 
<hr>   
np.random.uniform(min,max,number of element) => return such array
<hr>
np.random.randn(10,10)=> samilar to random.random. diff is take 2 argument while random.random take a tuple.
<hr>
array.max()  // array.min() // array.mean() 
<hr>
np.pad(array,pad_width=1,mode='constant',constant_values=0)
<hr>
z=np.diag(vector to go on diag line,k=-1) if k=-1,oneline under diag if k=1,1 line over diag
<hr>
np.unravel_index(target vector,shape) => np.unravel_index([33,23,22],(6,7,8))
<hr>
np.tile(example of array,(size of new array)) =>> return a array with copy of example array
<hr>
np.dot(arrayA,arrayB) => matrix multiply
<hr>    
sum(iter,-1) => -1 means start from -1// np.sum(iter,-1) => -1 means axis
<hr>    
yesterday=np.datetime64('today','D')-np.timedelta(1,'D')
<br>today = np.datetime64('today','D')
<br>np.arange('yyyy-mm','end yyyy-mm',dtype=datetime64[D])   =>return all date within this period
<hr>
inline operation 
<br>np.add(a,b,out=b)/ np.divide(a,b,out=b) / np.negative(a,out=a) / np.multiply(a,b,out=b)
<hr>
convert matrixto int from float
<br>float_array.astype(int)   / np.floor(float_array)-1  / np.ceil(float_array)
<hr>    
create vector from generator
<br>np.fromiter(generator(),dtype=float,count=-1)
<hr>
np.linspace(0,1,11,endpoint=False) =>return array that has the same diff between each near elements
<hr>
np.add.reduce(array)  is faster than np.sum(array) ==>>because in numpy, add.reduce is called when sum is called.