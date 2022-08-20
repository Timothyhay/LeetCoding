import numpy as np
import pandas as pd

## Series

# Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
# Series 由索引（index）和列组成，函数如下：
# pandas.Series( data, index, dtype, name, copy)
'''
data：一组数据(ndarray 类型)。
index：数据索引标签，如果不指定，默认从 0 开始。
dtype：数据类型，默认会自己判断。
name：设置名称。
copy：拷贝数据，默认为 False。
'''
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)

# pandas.DataFrame( data, index, columns, dtype, copy)
'''
data：一组数据(ndarray、series, map, lists, dict 等类型)。
index：索引值，或者可以称为行标签。
columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
dtype：数据类型。
copy：拷贝数据，默认为 False。'''

# Use list to init
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# Use dict to init, key will be the field name
data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}

df0 = pd.DataFrame(data, columns=['Site', 'Age'])

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]  # This will make row 0 col 'c' NaN


# print(df0)

# 使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：
days = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(days, index=["day1", "day2", "day3"])

# 指定索引
print(df.loc["day2"])
print(df0.loc[1])
# 返回结果其实就是一个 Pandas Series 数据。

# 也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开：
print("Multi-line:")
print(df0.loc[[0, 1]])
# 返回结果其实就是一个 Pandas DataFrame 数据。
# 当然连续多行也可以： e.g. 0~1 row
print(df0.loc[0:1])


