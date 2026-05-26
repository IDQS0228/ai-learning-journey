""" 
def 函数名(参数):      # def 关键字 + 名字 + 括号（参数可空）
    函数体代码          # 缩进！具体干活的逻辑
    return 返回值       # 结果返回给调用者（可选） 
"""

#所谓的编程本体

#无参数函数
def print_line():   #定义
    print("-"*30)

print_line()  #执行

#带参数函数
def add_now(x,y):   #定义
    z=x+y
    return(z)

add_num = add_now(3,9)
print("带参数函数结果",add_num)

