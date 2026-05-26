#列表 = 能装多个数据、可改、有序、能混装的 “容器”

#空列表创建
a = []
b = list()

#直接创建元素
fruits = ["苹果","香蕉","橙子","葡萄"]
nums = [10,20,20]
mix = [1, "hello", True, 3.14] #可混合元素

#用 range 生成数字列表
r = list(range(5))      # [0,1,2,3,4]
r2 = list(range(2, 10, 2)) # [2,4,6,8]
r3 = list(range(3,50,5))
print(r3)


#查询，索引
print(fruits[0])   # 苹果（第1个）
print(fruits[2])   # 橙子（第3个）
print(fruits[-1])  # 葡萄（最后一个）
print(fruits[-2])  # 橙子（倒数第二个）

#增加元素
#append：末尾加
#insert：指定位置加
#extend：批量加
fruits = ["苹果", "香蕉"]

#append
fruits.append("橙子")
print(fruits)

#insert
fruits.insert(1,"芒果")
print(fruits)

#extend
fruits.extend(["葡萄","西瓜"])
print(fruits)


#直接更改元素
fruits[0] = "蓝莓"
print(fruits)

#删除元素
#pop()：按照索引删除（默认最后一位）
#remove：按值删（删第一个匹配的）
#clear：清空列表元素

#pop
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)

#remove
fruits.remove("芒果")
print(fruits)

#clear
fruits.clear()
print(fruits)


#len元素数量
#max最大值
#min最小值
#sum求和
nums = [10, 20, 5, 30, 15]
print(len(nums))   # 长度：5
print(max(nums))   # 最大：30
print(min(nums))   # 最小：5
print(sum(nums))   # 求和：80

#sort小到大排序
nums.sort()
print(nums)
#reverse反转
nums.reverse()
print(nums)
