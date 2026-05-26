"""

 if 条件1:
    # 条件1 True
elif 条件2:
    # 条件1 False、条件2 True
elif 条件3:
    # …
else:
    # 所有条件都 False 

"""

""" 
if 条件:
    # 条件为 True 时执行（必须缩进，一般4空格）
    语句 
"""

#定义x
x = 10
if x>10:
    print(x) #无输出

x=11
if x==11:
    print(x) #输出11

score = 78
if score==100:
    print("A")
elif score>=80:
    print("B")
elif score>=60:
    print("C")
else:
    print("E")
    #C