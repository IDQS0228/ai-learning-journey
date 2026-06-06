# 数组变形 reshape + 数组运算 +聚合统计
import numpy as np

# reshape 维度重塑（元素总数必须匹配）
arr = np.arange(16)
print(arr)
arr2 = arr.reshape(4,4)     # 把数组改成4×4的二维表
print(arr2)

# 自动计算行数，-1自动适配
arr3 = np.arange(27).reshape(-1,3)  #固定了列数为3，行数自适应
print(arr3)

print("---------------------")

# 同现状数组四则运算 （对应位置元素相互运算）
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,20,30],[40,50,60]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("---------------------")

arr = np.array([[1,2,3],[4,5,6]])
print(arr.max())    # 全局最大值
print(arr.min())    # 全局最小值
print(arr.sum())    # 全局求和
print(arr.mean())   # 全局平均值
print(arr.sum(axis=0))      # axis=0：按列计算
print(arr.sum(axis=1))      # axis=1：按行计算