import numpy as np

print("===== 1. 矩阵转置 A.T =====")
# 对应手写转置第1题
A = np.array([[1,3,-2],
              [0,4,1]])

A_T = A.T
print("原矩阵A shape", A.shape, "\n", A)
print("转置A^T shape", A_T.shape, "\n", A_T)

# 对称矩阵演示
C = np.array([[1,2],
              [2,5]])
print("\n对称矩阵C：\n", C)
print("C转置：\n", C.T)

print("\n===== 2. 计算方阵行列式 np.linalg.det() =====")
# 手写行列式二阶行列式
mat2 = np.array([[2,3],
                 [1,5]])
det2 = np.linalg.det(mat2)
print(f"二阶矩阵行列式 = {det2:.2f}")

# 手写三阶行列式第3题
mat3 = np.array([[1, 0, 2],
                 [3, 1, -1],
                 [0, 2, 4]])
det3 = np.linalg.det(mat3)
print(f"三阶矩阵行列式 = {det3:.2f}")

print("\n===== 3. 可逆矩阵求逆 + 验证 A·A⁻¹ = 单位矩阵 =====")
# 可逆矩阵
A_inv_mat = np.array([[3,1],
                      [2,4]])
det_A = np.linalg.det(A_inv_mat)
print(f"A行列式 det(A)={det_A:.2f}，det≠0 矩阵可逆")

A_inv = np.linalg.inv(A_inv_mat)
print("A逆矩阵 A⁻¹：\n", A_inv)

# 验证 A @ A⁻¹ = 单位矩阵
verify = A_inv_mat @ A_inv
print("A × A⁻¹ 验证（单位矩阵）：\n" , np.round(verify,6))

print("\n===== 4. 奇异矩阵求逆（报错演示） =====")
singular_mat = np.array([[2, 4], [1, 2]])
# det_s = np.linalg.inv(singular_mat)
# print(f"奇异矩阵行列式 det={det_s:.2f}，不可逆")
try:
    res = np.linalg.inv(singular_mat)
except np.linalg.LinAlgError as e:
    print("捕获报错：", e)
