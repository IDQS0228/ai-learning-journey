# 继承→封装→多态



# 狗 父类
class dog:
    # 构造函数
    def __init__(self, name ):
        self.name = name 

    #方法
    def show(self):
        print(f"我是狗，名字是{self.name}")

# 西施犬 子类
class west_lion(dog):
    #构造函数
    def __init__(self, name , size):
        super().__init__(name)    #调用父类的构造函数super().__init__(参数)
        self.__size = size

    def show(self):     #重写方法
        print(f"我是狗，名字是{self.name},我是一只{self.__size}")

# 马尔济斯
class mar(dog):
    #构造函数
    def __init__(self,name,size):
        super().__init__(name)
        self.__size = size

    def show(self):
        print(f"我是狗，名字是{self.name},我是一只{self.__size}")

d1 = dog("小金毛")
d1.show()
print(d1.name)

w1 = west_lion("小燕子","小型犬")
w1.show()

m1 = mar("小小白","小型犬")
m1.show()



class ani:
    # 构造函数
    def __init__(self,type):
        self.type = type

    def show2(self):
        print("我是{self.type}")

class goldDog(ani,dog):
    def __init__(self , name ,type):
        # super().__init__(type,name)是错误的，只能调用一个参数
        super().__init__(type)
        self.name = name
    
    def show2(self):
        print(f"我是{self.type}，名字是{self.name}")

g1 = goldDog("犬科","小鸡毛")
g1.show2()

    
    

