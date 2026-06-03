class Person:
    #构造函数：定义类的属性，创建对象自动执行
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(f"我叫{self.name},今年{self.age}岁了，来自{self.address}")