import pandas as pd
import numpy as np

# 1. 复用之前清洗好的原始脏数据，先做完整清洗流程
dirty_data = {
    "商品": ["螺丝刀", "扳手", "钳子", "螺丝钉", "扳手", None, "螺丝刀"],
    "单价": [15.5, 25.0, np.nan, 1.0, 25.0, 18.0, 15.5],
    "库存": [120, 80, 95, np.nan, 80, 380, 120]
}
df = pd.DataFrame(dirty_data)
fill_rule = {
    "商品": "未知商品",
    "单价": df["单价"].mean(),
    "库存": 0
}
df_clean = df.fillna(fill_rule)
df_clean = df_clean.drop_duplicates(subset=["商品", "单价", "库存"], keep="first")
print("===== 清洗完成的干净数据表 =====")
print(df_clean)

# ====================== 1. 新增衍生计算列 ======================
# 新增一列（总金额 = 单价 * 库存）
print("===== 新增一列（总金额 = 单价 * 库存） =====")
df_clean["总金额"] = df_clean["单价"] * df_clean["库存"]
print(df_clean)

# ====================== 2. sort_values() 数据排序 ======================
# 按库存升序（从小到大）
df_sort_asc = df_clean.sort_values(by = "库存" ,ascending = True)
print("2.1 按库存升序排列（少→多）")
print(df_sort_asc)

# 按总金额降序（从大到小）
df_sort_desc = df_clean.sort_values(by = "总金额" , ascending = False)
print("\n2.2 按总金额降序排列（多→少）")
print(df_sort_desc)

print("-----------------------------------------")

# 构造【多条重复商品】的五金进货数据（同一商品有多条入库记录，完美体现分组汇总）
stock_data = {
    "商品": ["螺丝刀", "扳手", "钳子", "螺丝钉", "螺丝钉", "手电钻", "扳手", "螺丝钉"],
    "单价": [15.5, 25.0, 18.0, 1.0, 1.2, 199.0, 24.5, 0.9],
    "库存": [120, 80, 95, 380, 500, 30, 60, 420]
}
sd = pd.DataFrame(stock_data)
sd["总金额"] = sd["单价"] *sd["库存"]
print(sd)

# ====================== 3. groupby 分组聚合统计（核心） ======================
# 3.1 基础分组：按商品分组，对数值列自动求和
group_sum = sd.groupby("商品").sum()
print("3.1 按商品分组，库存、总金额求和汇总")
print(group_sum)

# 3.2 自定义聚合：同时计算 总和、平均值、数量 agg
group_agg = sd.groupby("商品").agg(
    总库存 = ("库存","sum"),
    平均单价 = ("单价","mean"),
    品类数量 = ("商品","count"),
    总货值 = ("总金额","sum")
)
print("\n3.2 分组多维度聚合统计")
print(group_agg)

# 3.3 筛选分组后数据：只看总库存大于100的商品
group_filter = group_agg[group_agg["总库存"] > 100]
print("\n3.3 筛选分组后总库存>100的商品")
print(group_filter)
