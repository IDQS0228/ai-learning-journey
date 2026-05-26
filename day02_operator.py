#学习运算符

# +  加
# -  减
# *  乘
# /  除
# // 整除（只取整数部分）
# %  取余（取余数）
# ** 次方（平方、立方等）

# == 等于
# != 不等于
# >  大于
# <  小于
# >= 大于等于
# <= 小于等于

# =   赋值
# +=  加等  a += 1 → a = a + 1
# -=  减等
# *=  乘等
# /=  除等

# and  并且
# or   或者
# not  非（取反）

#定义ab变量的值
a = 10
b = 3

print(a+b) #13
print(a-b) #7
print(a*b) #30
print(a/b) #3.33333333
print(a//b) #3
print(a%b) #1
print(a**b) #100

print(a==b) #f
print(a!=b) #t
print(a>b) #t
print(a<b) #f
print(a>=b) #t
print(a<=b) #f


x=4
print(x) #4
x+=2
print(x) #6
x-=4
print(x) #2
x*=5
print(x) #10
x/=4
print(x) #2.5


print(False and True)
print(False or True)
print(not False)