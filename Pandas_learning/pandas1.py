import pandas as pd     # 标准写法
import numpy as np



# 一列数据（一维）
s = pd.Series([10,20,30,40], name = "分数")
print("Series 一列数据")
print(s)

# 表格（二维）
data = {
    "名字": ["张三","李四","王五","赵六"],
    "年龄": [18,19,20,18],
    "成绩": [90,89,77,98]
}

# 字典转pd表格
df = pd.DataFrame(data)
print("\nDataFrame 完整表格")
print(df)



# 数据查看
print("\n查看前两行数据")
print(df.head(2))

print("\n查看表格形状")
print(df.shape)

print("\n查看每列信息")
print(df.info())

print("\n数据统计")
print(df.describe())