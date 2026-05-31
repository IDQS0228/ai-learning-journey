# **kwargs 打包成字典的关键字参数
# 接受任意多个 键值对 形式的参数，并且打包成字典{}
# *args 区别：返回是元组()

# **kwargs 示例：
# **lwarhs 把传入的关键词参数打包成字典
def info(**kwargs):
    print("kwargs的数据类型： ",type(kwargs))
    print(kwargs)

# 调用
info(name ="张三" , age = 18 , gender = "男")
info(score = 90 , city = "广州")

# 遍历kwargs
def info(**kwargs):
    for k , v in kwargs.items():
        print(f"{k}:{v}")
info(name="李四", age=20, hobby="打球")


# 常识：
# 局部变量：是在函数里产生，定义的变量，只能在函数里使用，函数结束后将不存在
def test():
    a = 10   # 局部变量
    print(a)

test()
# print(a)  # 这里会报错，外面访问不到

# 常识：
# 全局变量：是在函数外定义的变量，执行到了定义语句后将在全局使用，即可被函数读取
# 在函数里修改的全局变量会在函数结束后变回原值
b = 20   # 全局变量
def test2():
    b = 10
    print(b)

test2()
print(b)

# global 关键词，可以在函数里修改全局变量
# 如果我在函数里调用全局变量x，只是在函数里设立了一个名字和值一模一样的局部变量x，但我用global声明了一下，就是直接调用的是外面的全局变量x
count = 0
def add_count():
    global count    #声明用全局变量
    count += 1

add_count()
print(count)