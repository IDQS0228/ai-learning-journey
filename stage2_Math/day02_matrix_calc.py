import numpy as np

print("===== 1. 创建不同维度矩阵 =====")
# 2*3普通矩阵
A = np.array([[1,2,-1],
              [3,0,4]])
# 2*3矩阵
B = np.array([[2,-1],
              [0,3],
              [1,2]])
# 2*2方阵
C = np.array([[2,1],
              [-1,3]])

# 2阶单位矩阵
I2 = np.eye(2)

print(f"A 形状{A.shape}:\n{A}")
print(f"B 形状{B.shape}:\n{B}")
print(f"C 单位矩阵I2：\n{I2}")


print("\n===== 2. 矩阵加法、数乘 =====")
C1 = np.array([[1, 2],
               [-1, 0]])
C2 = np.array([[3, -4],
               [2, 5]])
add_res = C1 + C2
mul_num_res = -2 * C1
print("矩阵加法 C1+C2：\n", add_res)
print("数乘 -2*C1：\n", mul_num_res)


print("\n===== 3. 两种乘法：标准矩阵乘 VS 哈达玛积 =====")
# 哈达玛积要求同维度
D1 = np.array([[1, 3], [2, -1]])
D2 = np.array([[4, 0], [-2, 5]])
hadamard = D1 * D2  # 逐元素相乘，哈达玛积
mat_mul = np.dot(A,B)   # 标准矩阵乘法
print("=== 哈达玛积 D1 * D2 ===")
print(hadamard)
print("=== 标准矩阵乘法 np.dot(D1,D2) ===")
print(mat_mul)