# 类（class）
# 对象（Object）

# class：定义类
# __init__：构造方法，创建对象自动运行
# self：代表当前对象自己




class computer:
    #构造方法
    def __init__(self,cpu,gpu):
        self.cpu = cpu
        self.gpu = gpu

    #方法
    def show(self):
        print(f"我的电脑的cpu是{self.cpu}，gpu是{self.gpu}")

c1 = computer("265k","5060")
c1.show



import Person

p1 = Person.Person("QS",24,"泰顺")
p2 = Person.Person("LY",22,"怀远")

p1.show()
p2.show()


print(p1.name,"的电脑是",c1.cpu)