import numpy as np
import math

# ====================== 1. 创建行向量、列向量 ======================
# 行向量 shape(1,n)
row_vec = np.array([[2,4,1]])
print("行向量：", row_vec)
print("行向量形状：", row_vec.shape)
# 列向量
col_vec = np.array([[1],[2],[3]])
print("\n列向量：\n", col_vec)
print("列向量形状：", col_vec.shape)


# ====================== 2. 向量加法、数乘 ======================
a = np.array([1,3,2])
b = np.array([4,-1,0])
vec_add = a + b
vec_mul = 2 * a
print("\n向量加法 a+b：", vec_add)
print("数乘 2*a：", vec_mul)
# ====================== 3. 进阶运算：点积、L1/L2范数、夹角 ======================
v1 = np.array([1,3])
v2 = np.array([4,2])
# 点积
dot_product = np.dot(v1,v2)
print("\n点积 v1·v2 =", dot_product)
# L1、L2 范数
l1_v1 = np.linalg.norm(v1, ord=1)
l2_v1 = np.linalg.norm(v1, ord=2)
l1_v2 = np.linalg.norm(v2, ord=1)
l2_v2 = np.linalg.norm(v2, ord=2)
print(f"v1 L1范数：{l1_v1:.2f}, L2范数：{l2_v1:.2f}")
print(f"v2 L1范数：{l1_v2:.2f}, L2范数：{l2_v2:.2f}")
# 计算夹角
cos_theta = dot_product / (l2_v1 * l2_v2)
rad_theta = math.acos(cos_theta)    #弧度
deg_theta = math.degrees(rad_theta) #转角度
print(f"夹角 弧度：{rad_theta:.3f}, 角度：{deg_theta:.2f}°")
