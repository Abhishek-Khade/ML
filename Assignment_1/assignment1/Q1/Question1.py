# 1. i) Create a list of empids and names (10 employees).
#    ii) Convert list into Series.
#    iii) Print type of Series.
#    iv) Convert Series into DataFrame.
#    v) a) Display all records.
#       b) Display first five records.
#       c) Display last five records.
#    vi) Save the record in csv file (MyRecord.csv)
import pandas as pd
empid=[1,2,3,4,5,6,7,8,9,10]
emp_names=['omkar','anant','abhishek','rahul','akash','ram','sam','pavan','sandy','tejas']
empid_names=pd.Series(emp_names,index=empid)
print(empid_names)
print(type(empid_names))

df=pd.DataFrame(empid_names)
print(df)
print(df.head())
print(df.tail())

save_file=df.to_csv('MyRecord.csv')
