import numpy as np      #常规np命名
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 索引取值
#   取整行
print(arr[0])   # 第0行 [1,2,3]
print(arr[2])   # 第2行 [7,8,9]
#   取单个元素[行,列]
print(arr[1,2])     #第1行，第2列[6]
print(arr[2,0])     #第2行，第0列[7]

# 切片语法：[行起始：行结束,列起始:列结束]
# 前2行，全部列
print(arr[:2,:])
# 全部行，前2列
print(arr[:,:2])
# 前2行，前2列
print(arr[:2,:2])

# 步长取值 start:end:step
arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1[2::2])