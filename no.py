import pandas as pd

dataframe = pd.read_table('train.csv')
print(dataframe)


for item in dataframe():
    print(item)
    