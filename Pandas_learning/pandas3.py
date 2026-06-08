import pandas as pd

# 读取库数据
df = pd.read_csv("data.csv",encoding="utf-8")
print("表格总行数：", len(df))

# 展示表格
print(df)



# 筛选列
print("---------单列提取-----------")
col_goods = df["商品"]  # 直接输入列名      单列筛选
print(col_goods)

print("---------多列提取-----------")
col_goods = df[["商品","单价"]]     # 多列筛选，双重括号
print(col_goods)

# 筛选行
print("---------行提取-----------")
# iloc：按数字位置取行（从0开始）
# loc：按自定义标签取行（默认标签就是0/1/2/3）
row_0 = df.iloc[0]      # 提取第0行
row_1_2 = df.iloc[1:3]  # 提取第1，2行，[1,3]指的是包括1直到不包括3
print("iloc取第0行：\n", row_0)
print("iloc取1~2行：\n", row_1_2)
row_loc = df.loc[2]
print("loc取索引2行：\n", row_loc)

print("---------布尔条件提取-----------")
stock_over_100 = df[df["库存"]>100]
print("库存>100的商品：")
print(stock_over_100)

multi_cond = df[(df["库存"]>100 )&(df["单价"]<20) ]
print("库存>100 且 单价<20：")
print(multi_cond)