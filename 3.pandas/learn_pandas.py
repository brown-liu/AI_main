import pandas as pd
import numpy as np
# Series is simliar to 1Darray
s=pd.Series([1,4,6,7,np.nan])
print(s)
dates=pd.date_range("20200909",periods=12)
print(dates)

dataframe=pd.DataFrame(np.random.rand(12,4),index=dates,columns=["startime","endtime","total","expense"])
print(dataframe)

# using list to create DataFrame

df2=pd.DataFrame(
    {
        'A':[i for i in range(10)],
        "B":pd.Timestamp('20200202'),
'C':pd.Series(1,index=[i for i in range(10)],dtype='float32'),
        'D':["superman","Kitkate","Boeing 747","superwoman",'Dog',"Unitec",'CAT',"Pig",'Move','Chick']   }
)
# dtypes give datatypes
print(df2.dtypes)

print(f"df2.head()==>\n {df2.head()} ,\n df2.tail() ==> \n {df2.tail()}")
print(f"df2.index ===>(Not a function, it is attribute) {df2.index}\ndataframe.index ===>(Not a function, it is attribute) {dataframe.index}")
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1,ascending=True))
print(df2.sort_values(by="D"))
print(df2['D'])
print(df2[0:3])
print(df2.loc[:,'D'])
print(df2.loc[:3,['A','D']])
print('iloc',df2.iloc[[1,2,3],3])
# difference between iloc and loc, loc must use index name or column name, iloc use index
print(df2[df2.A>3])
# can apply some function to work on data
print(df2.apply(np.cumsum))
print(np.cumsum(np.array([[i for i in range(5)] for i in range(5)])))
print([[i for i in range(5)] for i in range(5)])