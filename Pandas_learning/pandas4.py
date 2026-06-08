import pandas as pd
import numpy as np
# 数据清洗（处理脏数据）

# 1. 构造带缺失值、重复行的脏数据（模拟真实业务脏表）
dirty_data = {
    "商品": ["螺丝刀", "扳手", "钳子", "螺丝钉", "扳手", None, "螺丝刀"],
    "单价": [15.5, 25.0, np.nan, 1.0, 25.0, 18.0, 15.5],
    "库存": [120, 80, 95, np.nan, 80, 380, 120]
}

df = pd.DataFrame(dirty_data)
print("===== 原始脏数据（含空值、重复行）=====")
print(df)

print("--------查看缺失值-------")
print("1. 查看每列缺失值数量")
print(df.isnull().sum())

print("--------删除缺失值 dropna()-------")
# how="any"：只要一行有任意空值，直接整行删除
df_drop_na = df.dropna(how="any")   # df.dropna(how="any")删除语句
print("2. 删除存在空值的所有行")
print(df_drop_na)

print("--------填充缺失值 fillna()-------")
# 方案1：全局统一填充（空值全部填0）
df_fill0 = df.fillna(0)
print("3.1 所有缺失值填充为0")
print(df_fill0)

# 方案2：按列针对性填充（单价空填平均值，库存空填0，商品空填未知）
fill_rule = {
    "商品": "未知商品",
    "单价": df["单价"].mean(),
    "库存": 0
}
df_fill_col = df.fillna(fill_rule)
print("\n3.2 按不同列自定义填充规则")
print(df_fill_col)


print("--------重复数据去重 drop_duplicates()-------")
# subset 指定按哪几列判断重复，keep="first" 保留第一条重复数据
df_distinct = df_fill_col.drop_duplicates(subset=["商品","单价","库存"],keep="first")
print("4. 删除完全重复的商品行，只保留第一条")
print(df_distinct)