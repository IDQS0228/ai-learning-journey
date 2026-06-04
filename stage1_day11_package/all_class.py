class Student:
    #构造函数
    def __init__(self,num,name,age):
        self.__num = num
        self.__name = name
        self.__age = age

    #修改学生信息函数
    def set_name(self , new_name):
        self.__name = new_name

    def set_age(self , new_age):
        # if isinstance(new_age,int):
        self.__age = new_age

    #获取学生信息函数
    def get_num(self):
        return self.__num
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def show(self):
        print(f"学号：{self.__num}|姓名：{self.__name}|年龄：{self.__age}")
    


class StudentManager:
    # 构造函数
    def __init__(self):
        self.student_list = []

    # 增
    def add_student(self, stu):
        self.student_list.append(stu)
        print("✅ 添加成功！")

    # 删
    def del_student(self, num):
        for stu in self.student_list:
            if stu.get_num() == num:
                self.student_list.remove(stu)
                print("删除成功!!!!")
                return
        print("❌ 未找到该学生")

    # 改
    def modify_student(self,num , new_name , new_age):
        for stu in self.student_list:
            if stu.get_num() == num:
                stu.set_name(new_name)
                stu.set_age(int(new_age))
                print("修改成功！！！！")
                return
            
        print("❌ 未找到该学生")

        

    # 查
    def find_student(self,num):
        for stu in self.student_list:
            if stu.get_num() == num:
                stu.show()
                print("查询成功！！！！")
                return
            
            
        print("❌ 未找到该学生")

        

    def show_all(self):
        for stu in self.student_list:
            stu.show()





    