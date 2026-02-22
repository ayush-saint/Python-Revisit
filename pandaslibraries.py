# Pandas is a Python library used for: data analysis, working with tables (rows and columns), reading csv/ Excel files, cleaning and organizing data 

import pandas as pd 

# getting tabular form of data by pandas 
df = {'people':['p1','p2','p3'], 'Age':[20,30,40]}
print(pd.DataFrame(df))

# getting only age 
print(df['Age'])



