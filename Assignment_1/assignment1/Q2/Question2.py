import pandas as pd

def function1():
    df=pd.read_csv('Advertising.csv')
    print(df.head())
    print(df.tail())
    print(df.columns)
    print(df.tail(3))
    df.info()
    print(df.dtypes)
    print(df.isna().sum())
    df.drop('radio',axis=1,inplace=True)
    print(df.head(10))
    print(df.dropna(axis=1,inplace=True))
    df['updated_sales']=df['sales']*0.10+df['sales']
    print(df)
    print(df.shape)



function1()

# increase the sales by 10% and add a new column "updated_sales" in dataframe.