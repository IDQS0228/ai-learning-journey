import pandas as pd
import matplotlib.pyplot as plt

""" 
# 泰坦尼克乘客数据 — 字典格式
titanic_data = {
    "PassengerId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Survived": [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    "Pclass": [3, 1, 3, 1, 3, 3, 1, 3, 3, 2],
    "Sex": ["male", "female", "female", "female", "male", "male", "male", "male", "female", "female"],
    "Age": [22, 38, 26, 35, 35, None, 54, 2, 27, 14],
    "SibSp": [1, 1, 0, 1, 0, 0, 0, 3, 0, 1],
    "Parch": [0, 0, 0, 0, 0, 0, 0, 1, 2, 0],
    "Fare": [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708]
}

df = pd.DataFrame(titanic_data)
df.to_csv("titanic.csv",index=False,encoding="utf-8")
 """


# 中文设置
plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

# 1.读取数据
df = pd.read_csv("titanic.csv")
print("原始数据：")
print(df.head())
print("统计缺失值")
print(df.isnull().sum())

# 2. 数据清洗：年龄缺失值用平均值填充
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 3. 统计分析
# 3.1 总存活/死亡人数
survive_count = df["Survived"].value_counts()
print("\n存活(1) / 死亡(0) 人数：")
print(survive_count)

# 3.2 各舱位人数
pclass_count = df["Pclass"].value_counts()

# 4. 绘图（至少3张图）
# 图1：存活人数柱状图
plt.figure(figsize=(6,4))
plt.bar(["死亡","存活"], survive_count.values, color=["gray","red"])
plt.title("乘客存活情况")
plt.show()

# 图2：不同舱位人数柱状图
plt.figure(figsize=(6,4))
plt.bar(df["PassengerId"],df["Pclass"],color="steelblue")
plt.title("各舱位乘客数量")
plt.xlabel("舱位ID")
plt.ylabel("人数")
plt.show()

plt.figure(figsize=(6,4))
plt.bar(pclass_count.index, pclass_count.values)
plt.title("各舱位乘客数量")
plt.xlabel("舱位等级")
plt.show()

# 图3：票价分布折线图
plt.figure(figsize=(6,4))
plt.plot(df["PassengerId"],df["Fare"],marker = "o",color = "orange")
plt.title("乘客票价分布")
plt.xlabel("乘客编号")
plt.ylabel("票价")
plt.show()