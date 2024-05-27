import pandas as pd

def function1():
    df=pd.read_csv('Salaries .csv')
    print(df.head())
    print(df.head(10))
    print(df.tail())
    print(df.tail(10))
    print(df.columns)
    print(df.shape)

    df.info()
    print(df.dtypes)
    print(df.describe())
    print(df.isna().sum())
    df['phd'].fillna(df['phd'].mean(),inplace=True)
    df['service'].fillna(df['service'].mean(),inplace=True)
    df['salary'].fillna(df['salary'].mean(),inplace=True)
    print(df.isna().sum())
function1()