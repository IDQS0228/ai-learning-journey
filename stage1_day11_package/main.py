import all_class   # 导入all_class

manager = all_class.StudentManager()

while True:
    print("""
        ====== 学生信息管理系统 ======
        1. 添加学生
        2. 删除学生
        3. 修改学生
        4. 查询学生
        5. 显示所有学生
        6. 退出系统
        """)
    
    choice = input("请输入您需要执行的编号")

    if choice == "1":
        num = input("请输入学生id：")
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄"))
        stu = all_class.Student(num,name,age)
        manager.add_student(stu)
    if choice == "2":
        num = input("请输入要删除的学生id：")
        manager.del_student(num)
    if choice == "3":
        num = input("请输入要修改信息的学生id")
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄"))
        manager.modify_student(num,name,age)
    if choice == "4":
        num = input("请输入要查询的学生id")
        manager.find_student(num)
    if choice == "5":
        manager.show_all()
    if choice == "6":
        print("退出系统")
        break
