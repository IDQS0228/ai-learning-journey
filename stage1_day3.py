# lambda 匿名函数（一句话函数）
# lambda 参数 : 表达式
# 返回的是表达式结果

# 对比普通函数
def add( a , b ):
    return a + b

# lambda函数
add_lambda = lambda a , b : a + b

# 调用
print(add( 2 , 3 ))
print(add_lambda(2 , 3))

# lambda应用场景
students = [("张三",35),("李四",88),("王五",23)]
students_sorted = sorted(students,key=lambda x : x[1])
print(students_sorted)


# map：对每个元素做同样操作
# filter：筛选元素（保留 True 的）
# sorted：排序（key 参数必用 lambda）

# map 举例
nums = [1,2,3,4]
# 普通写法
res = [x**2 for x in nums]
print(res)
# map 对迭代的的对象全部都进行相同的操作，因此可以看作对list的操作
res = list(map(lambda x: x**2, nums))
print(res)  # [1,4,9,16]

# filter 举例
nums = [1,2,3,4,5]
evens = list(filter(lambda x : x % 2 == 0 ,nums))
print(evens)

# sorted 举例
words = ["apple", "hi", "banana"]
sorted_words = sorted( words , key = lambda x : len(x))
print(sorted_words)





# 常见的几种内置函数组合
# max/min (key+lambda)
data = [("张三",35),("李四",88),("王五",23)]
best = min( data , key = lambda x : x[1])
print(best)

# zip ： 打包成元组对
a = [1,2,3]
b = ["x","y","z"]
zip_a_b = list(zip(a,b))
print(zip_a_b)

# eval：字符串转表达式（慎用！）
print(eval("1+2*3"))  # 7