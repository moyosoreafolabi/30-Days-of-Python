# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
import pandas as pd
import numpy as np

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# creating Panda series from a dictionary
dct = {'name':'Moyosore','country':'Nigeria','city':'Lagos'}
s = pd.Series(dct)
print(s)

s = pd.Series(10, index = [1, 2, 3])
print(s)

data = [
    ['Moyosore', 'Nigeria', 'Nigeria'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# creating dataframe using dictionary
data = {'Name': ['Moyosore', 'David', 'John'], 'Country':[
    'Moyosore', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# creating a dataframe
import pandas as pd
import numpy as np
data = [
    {"Name": "Moyosore", "Country":"Nigeria","City":"Lagos"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# adding a new column

weights = [74, 78, 69]
df['Weight'] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()
