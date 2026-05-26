#循环语句学习

#for循环
""" 
for i in range(5):
    print("循环执行中", i)
"""

x = 5   #定义循环次数
for i in range(x):
    print("for循环中",i,"次")
print("i最终值",i)



#while循环
""" 
i = 0
while i < 5:
    print("while 循环", i)
    i = i + 1   # 必须更新变量，否则死循环
 """

n = 0
while n<5:
    print("while循环中",n,"次")
    n+=1
print("n最终值",n)


# break → 立刻停止循环
# continue → 跳过本次，继续下一次

#break举例
for x in range(10):
    if x==5:
        break
    print("break示例中",x)

#continue举例
for x in range(10):
    if x==5:
        continue
    print("continue示例中",x)