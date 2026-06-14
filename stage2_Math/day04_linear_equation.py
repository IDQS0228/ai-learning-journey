import numpy as np

print("========= 1. 场景1：唯一解方程组 Ax=b =========")
# 对应手写唯一解例题：x+3y=5, 2x-y=1
A1 = np.array([[1,3],
               [2,-1]])
b1 = np.array([[5],[1]])
det_A1 = np.linalg.det(A1)

print(f"系数矩阵行列式 det={det_A1:.2f} ≠0，存在唯一解")
# 求解 x = A⁻¹b
x1 = np.linalg.inv(A1) @ b1
print("方程组解 x1, x2：\n", x1)
# 验证 A@x == b
verify1 = A1 @ x1
print("验证 A*x：\n", verify1)

print("\n========= 2. 场景2：无解方程组 =========")
# 2x-y=1, 4x-2y=3
A2 = np.array([[2,-1],
               [4,-2]])
b2 = np.array([[1],[3]])
# det_A2 = np.linalg.inv(A2)        # 尝试直接求逆会报错
# print(f"det={det_A2:.2f} ≈0，矩阵奇异")
try:
    x2 = np.linalg.inv(A2) @ b2
except np.linalg.LinAlgError as e:
    print("捕获报错：奇异矩阵无法求逆，方程组无解")

print("\n========= 3. 场景3：无穷多解方程组 =========")
# x+y=2, 2x+2y=4
A3 = np.array([[1, 1],
               [2, 2]])
b3 = np.array([[2], [4]])
det_A3 = np.linalg.det(A3)
print(f"det={det_A3:.2f} ≈0，奇异矩阵")
try:
    x3 = np.linalg.inv(A3) @ b3
except np.linalg.LinAlgError:
    print("矩阵不可逆，方程组有无穷多解，存在自由变量")