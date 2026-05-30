#建立一个存储学生的列表
students = []
pass_student = []

def add_student():  #录入学生信息函数
    name = input("输入学生名字：")
    china_score = int(input("输入学生语文成绩："))
    math_score = int(input("输入学生数学成绩："))
    english_score = int(input("输入学生英语成绩："))

    student = {
        "name":name,
        "scores":{
            "语文": china_score,
            "数学": math_score,
            "英语": english_score
        }
    }

    students.append(student)
    print("录入完成")

def avg_passed(students):
    total = 0
    china = 0
    math = 0
    english = 0
    for stu in students:
        scores = stu["scores"]
        total += scores["语文"] + scores["数学"] + scores["英语"]
        china += scores["语文"]
        math += scores["数学"]
        english += scores["英语"]
    total_avg = total / len(students)
    china_avg = china / len(students)
    math_avg = math / len(students)
    english_avg = english / len(students)
    print("总平均分：",total_avg,"语文平均分",china_avg,"数学平均分",math_avg,"英语平均分",english_avg)

def filter_passed(students):
    for stu in students:
        scores = stu["scores"]
        avg = (scores["语文"] + scores["数学"] + scores["英语"])/3
        if avg >60:
            pass_student.append(stu["name"])
    print("过60平均分名单",pass_student)

def all_students_score(students):
    for stu in students:
        print(stu["name"],"语文",stu["scores"]["语文"],"数学",stu["scores"]["数学"],"英语",stu["scores"]["英语"])


#学生系统：
print("1.录入学生信息：学生姓名 + 多门科目成绩（语文、数学、英语）  2.批量录入：可以一次录入多个学生  3.计算平均分：每个学生的总分、平均分  4.成绩筛选：找出平均分≥60 分的学生      5.打印所有学生信息：按格式输出  其他.结束")    
while True:
    x = int(input())
    if x==1:    #录入学生信息
        add_student()
    elif x==2:  #批量录入
        while True:
            add_student()
            add_continue=int(input("是否继续"))
            if add_continue==1:
                continue
            else:
                break
    elif x==3:  #计算平均分
        avg_passed(students)
    elif x==4:  #筛选
        filter_passed(students)
    elif x==5: #打印所有学生信息
        all_students_score(students)
    else:
        break



