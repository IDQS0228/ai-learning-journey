# 合并、分割、缺失值
import numpy as np

# 合并-----------------------------
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6]])

# 合并成行
d = np.concatenate([a,b],axis=0)        # axis=0合并成行
print(d)
d2 = np.vstack([a,b])
print(d2)
print("---------")

# 合并成列
e = np.concatenate([a,b.T],axis=1)      # axis=1合并成列    T：把b行列转置
print(e)
e2 = np.hstack([a,b.T])
print(e2)
print("----------------")


# 分割-----------------------------
x = np.arange(9)
print(x)

# 等分
y = np.split(x,3)
print(y)
# 确定位置选取
z = np.split(x,[3,6])
print(z)

print("---------------------")
# 二维分割
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])
print(arr)

# 上下切割
r1,r2 = np.split(arr , 2,axis=0)
print(r1)
print(r2)

# 左右切割
c1,c2,c3 = np.split(arr,3,axis=1)
print(c1)
print(c2)
print(c3)



print("-------------------")
# np.nan缺失值的处理    not a number
# 任何值和nan的运算都是nan
# 返回np.nan的位置
a = np.array([1,2,3,np.nan,4,5])
print(np.isnan(a))      #返回的是bool

# 统计时跳过np.nan
print(np.mean(a))   # mean对数组取平均值，不跳过np.nan，则运算会返回nan
print(np.nanmean(a))    # 加上nan则不会有问题
# nanmin = amin
# nanmax = amax
# nanargmin = argmin
# nanargmax = argmax
# nansum = sum
# nanprod = prod
# nancumsum = cumsum
# nancumprod = cumprod
# nanmean = mean
# nanvar = var
# nanstd = std
# nanmedian = median
# nanpercentile = percentile
# nanquantile = quantile

print("-------------------")
# 删除带有np.nan的行和列
data = np.array([[1,2,3],
                 [4,5,np.nan],
                 [7,8,9]])
print(data)

# 找出带有np.nan的行
bad_rows = np.where(np.isnan(data))[0]
print(bad_rows)
# 删除行
clean = np.delete(data,bad_rows,axis=0)
print(clean)

# 找出带有np.nan的列
bad_lies = np.where(np.isnan(data))[1]
clean_lies = np.delete(data,bad_lies,axis=1)
print(clean_lies)
