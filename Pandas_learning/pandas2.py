# 数据文件读写（CSV/Excel）
import pandas as pd

# # 读取CSV文件
# df = pd.read_csv("data.csv")

# # 查看前5行
# print(df.head())

# df = pd.read_csv("data.csv",sep = ",",encoding="utf-8",header=0,index_col=0)
# print(df.head())
# # 常用参数
# # sep: 指定分隔符（默认是逗号）
# # encoding: 处理中文乱码，常用 encoding="utf-8" 或 "gbk"
# # header: 指定表头行，默认是第0行
# # index_col: 指定某列作为索引

# df.to_csv("output.csv",index=False,encoding="utf-8")



# # 读取Excel文件
# df2 = pd.read_excel("data.xlsx",sheet_name="Sheet1")
# print(df2)

# df2.to_excel("output.xlsx",index=False,sheet_name="数据结果")

data = {
    "商品": ["螺丝刀", "扳手", "钳子", "电钻"],
    "单价": [15.5, 25.0, 18.0, 199.0],
    "库存": [120, 80, 95, 30]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("五金价目表.csv",index=False,encoding="utf-8")
df.to_excel("五金价目表.xlsx",index=False,sheet_name="库存价目表")
