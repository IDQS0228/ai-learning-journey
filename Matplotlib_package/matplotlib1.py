import matplotlib.pyplot as plt     # 常用写法
import pandas as pd

# 1.全局设置：解决中文显示 + 负号显示问题
plt.rcParams["font.family"] = "SimHei"  # 黑体
plt.rcParams["axes.unicode_minus"] = False      # 开启中文字体后，负号（如 -10、-50）会变成方框乱码；这行代码关闭 Unicode 负号渲染，让负数符号正常显示

# 复用之前的数据
data = {
    "商品" : ["螺丝刀", "扳手", "钳子", "螺丝钉"],
    "单价": [15.5, 25.0, 18.0, 1.0],
    "库存": [120, 80, 95, 380]
}
df = pd.DataFrame(data)


# 1. plt.figure() 的作用（隔离不同图表）
# 2. plt.show() 清空缓存机制


# ---------------- 1. 柱状图：展示各商品库存 ----------------
plt.figure(figsize=(8 ,5 ))     # 设置画布大小
plt.bar(df["商品"],df["库存"],color="steelblue")
plt.title("各商品库存数量")     # 标题
plt.xlabel("商品")      # x轴标题
plt.ylabel("库存数量")  # y轴标题
plt.show()

# ---------------- 2. 散点图：单价 & 库存关系 ----------------
plt.figure(figsize=(8,5 ))       
plt.scatter(df["单价"],df["库存"],s=80,color="orange")      # s= 点的大小
plt.title("单价与库存分布")
plt.xlabel("单价（元）")
plt.ylabel("库存数量")
plt.show()

# ---------------- 3. 折线图：单价走势 ----------------
plt.figure(figsize=(8,5 ))      
plt.plot(df["商品"],df["单价"],marker="o",color="green")
plt.title("商品单价折线图")
plt.xlabel("商品")
plt.ylabel("单价（元）")
plt.show()

# 写法	        形状
# marker="o"	实心小圆（你现在用的）
# marker="s"	正方形
# marker="^"	上三角
# marker="v"	下三角
# marker="*"	五角星
# markersize=   单独控制点大小

# ---------------- 4. 饼图：库存占比 ----------------
plt.figure(figsize=(6,6))
plt.pie(df["库存"], labels=df["商品"], autopct="%1.1f%%")
plt.title("各商品库存占比")
plt.show()

# %1.1f：浮点数，保留1 位小数
    # %1.0f%%：百分比保留整数，如 38%
    # %1.2f%%：保留两位小数，如 38.24%
# 末尾两个%%：最终输出一个百分号%
# 举例：计算出占比 38.2 → 图上显示 38.2%