import pandas as pd

urf = 'http://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

df = pd.read_csv(urf)

print(df.columns)

print(df.head())