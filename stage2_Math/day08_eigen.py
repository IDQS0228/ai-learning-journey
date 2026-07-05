import numpy as np

def eigen_calc(mat , name = "矩阵"):
    print(f"\n===== {name} 特征分解结果 =====")
    print(f"原矩阵：\n{mat}")
    # eigvals：特征值；eigvecs：每一列是一组特征向量
    eigvals , eigvecs = np.linalg.eig(mat)
    print(f"所有特征值 λ：{eigvals}")
    print(f"特征向量矩阵（每列为对应特征向量）：\n{eigvecs}")
    # 验证 A @ x = λ * x
    for i in range(len(eigvals)):
        lam = eigvals[i]
        vec = eigvecs[:,i:i+1]
        left = mat @ vec
        right = lam * vec
        print(f"\n验证第{i+1}组 λ={lam:.2f}:A@x ≈ λ*x")
        print("A@X : ",left.T[0])
        print("λ*x : ",right.T[0])
        return eigvals,eigvecs
    
A = np.array([[2,1],
              [1,2]])
B = np.array([[3,0],
              [0,2]])
eigen_calc(A,"手写矩阵A")
eigen_calc(B, "手写矩阵B")

# 2. 额外测试三阶方阵
M3 = np.array([[1, 2, 0],
               [2, 1, 0],
               [0, 0, 3]])
eigen_calc(M3, "三阶测试矩阵")