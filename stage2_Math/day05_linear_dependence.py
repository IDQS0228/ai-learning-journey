import numpy as np

def judge_linear_dep(vec_list):
    """
    输入向量列表，自动拼接矩阵、求秩、判断线性相关/无关
    :param vec_list: 一维数组组成的向量组
    :return: 秩r, 向量数量k, 判断结果字符串 
    """
    # 将向量作为列拼接成矩阵
    A = np.column_stack(vec_list)
    k = len(vec_list)
    # 计算矩阵秩
    r = np.linalg.matrix_rank(A)
    print(f"拼接矩阵：\n{A}")
    print(f"向量总个数 k = {k}")
    print(f"矩阵秩 rank(A) = {r}")
    if r == k:
        res = "线性无关"
    else:
        res = "线性相关"
    print(f"判定结论：{res}\n")
    return r, k, res

print("===== 例题1：v1=[1,2], v2=[3,4] =====")
v1 = np.array([1, 2])
v2 = np.array([3, 4])
judge_linear_dep([v1, v2])

print("===== 例题2：v1=[2,-1], v2=[4,-2] =====")
v3 = np.array([2, -1])
v4 = np.array([4, -2])
judge_linear_dep([v3, v4])

print("===== 例题3：v1=[1,0,1],v2=[0,1,2],v3=[1,1,3] =====")
v5 = np.array([1, 0, 1])
v6 = np.array([0, 1, 2])
v7 = np.array([1, 1, 3])
judge_linear_dep([v5, v6, v7])