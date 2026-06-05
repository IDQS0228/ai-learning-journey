import numpy as np  # 行业标准写法

# 测试部署
print(np.array([1,2,3])+5)

# 吧列表转numpy数组
# 普通列表
lst = [1,2,3,4,5]

# 转 numpy 数组
arr = np.array(lst)

print(arr)
print(type(arr))        #<class 'numpy.ndarray'>

# numpy 数组可以直接做数学运算（列表做不到！）
# 这就是 numpy 最强之处：整列批量运算
print(arr + 10)     # 每个元素 +10
print(arr * 2 )     # 每个元素 ×2
print(arr ** 2)     # 每个元素 平方

# 创建常用数组
# 0~9 数字
arr1 = np.arange(10)
print(arr1)
# 全 0 数组
arr2 = np.zeros(6)
print(arr2)
# 全 1 数组
arr3 = np.ones(5)
print(arr3)
# 随机数数组
arr4 = np.random.rand(5)
print(arr4)

# 数组属性（必背）
arr = np.array([[1,2,3],[3,4,5],[3,4,5],[3,4,5]])

print(arr.shape)    # 现状（几行几列）
print(arr.ndim)     # 维度
print(arr.dtype)    # 数据类型