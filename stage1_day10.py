# 封装
class dog:
    def __init__(self , name , age):
        self.name = name
        self.__age = age        # __age私有，外部不能obj.__age
    
    # get：获取私有属性
    def get_age(self):
        return self.__age
    
    # set：修改私有属性，加逻辑校验
    def set_age(self,new_age):
        if isinstance(new_age , int) and 0 < new_age <= 25:
            self.__age = new_age
        else:
            print("年龄非法！只能0~25的整数")

    def show(self):
        print(f"名字:{self.name},年龄:{self.__age}")


d = dog("燕子",2)

# 通过函数获取私有属性
print(d.get_age())
# print(d.__age)      #私有属性不能直接引用   #AttributeError: 'dog' object has no attribute '__age'

# 通过修改属性函数修改私有属性
d.set_age(1)
print(d.get_age())