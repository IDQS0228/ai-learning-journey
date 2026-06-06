import numpy as np

a = np.array([[1,2],
             [3,4]])
b = np.array([[5,6],
              [7,8]])

print("元素乘法 *：")
print(a * b)
# [[ 5 12]
#  [21 32]]

print("矩阵乘法 @：")
print(a @ b)
# [[19 22]
#  [43 50]]

# *：对应位置相乘（同形状才能算）
# @ / np.dot()：真正矩阵乘法，规则：
# (m,n) × (n,p) → (m,p)

print("-----------[广播]-------------")
# 标量 自动广播到全数组
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr + 10)     #每个元素都 +10

# 一维 + 二维
a = np.ones((3,4))   # (3,4)
b = np.array([0,1,2,3])  # (4,)
c = a + b
print(c.shape)  # (3,4)
print(c)

print("-----------[布尔索引]-------------")
arr = np.array([1,2,3,4,5,6])

mask = arr > 3      # 索引
print(mask)         # 返回bool数据类型的数组
print(arr[mask])    # 数组[bool数组] 返回True的数组排列

# 多条件（& 与、| 或）
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[(arr>2) & (arr<6)])

print("-----------------")
# 二维数组
arr = np.arange(12).reshape(4,3)
print(arr)
print(arr[arr[:,1]>5])      # 选出第二列大于5的 行

print("-------随机数进阶（整数、正态分布）---------")
# 随机整数
# [0，10） 之间，5个整数
r1 = np.random.randint(0,10,size=5)
print(r1)

# 正态分布（均值 loc、标准差 scale）
r2 = np.random.normal(0,1,size=(2,3))
print(r2)

r3 = np.random.normal(10,2,size= 5)
print(r3)