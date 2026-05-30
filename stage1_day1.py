# 函数默认参数
# 定义：给参数一个默认值
# f"{使用的默认值}"     f是格式化字符
def say_hello(name="同学"):
    print(f"你好，{name}")

# 调用
say_hello()          # 使用默认值
say_hello("小明")    # 使用传入值




# 函数返回多个值
# 返回的数据类型 :元组

def calc(a, b):
    add = a + b
    sub = a - b
    return add, sub

a1, a2 = calc(10, 3)
print("和：", a1)   # 和： 13
print("差：", a2)   # 差： 7

result = calc(10, 3)
print(type(result))  # 输出：<class 'tuple'>




# 可变参数 *args（传入任意多个参数）
# *args 可以接收 0、1、2、3... 无数个数字
# *args = 自动把一堆参数打包成元组的语法糖
def get_type(*args):
    for n in args:
        print(n,"的数据类型:",type(n))
    print(args,"的数据类型:",type(args))
        
get_type(1, 'abc', 3.14, True, [1, 2, 3])



# 用别人写好的功能
import random
# 使用import应用的random方法
num = random.randint(1, 100)
print("随机数：", num)
