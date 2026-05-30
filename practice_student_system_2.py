# 初始化学生列表（仅保留必要的全局变量）
students = []

def add_student():
    """录入单个学生信息（含输入合法性校验）"""
    # 姓名校验（简单非空）
    while True:
        name = input("请输入学生名字：").strip()
        if name:
            break
        print("姓名不能为空，请重新输入！")
    
    # 成绩校验（数字+非负）
    def get_valid_score(subject):
        while True:
            try:
                score = int(input(f"请输入学生{subject}成绩："))
                if 0 <= score <= 100:
                    return score
                else:
                    print(f"{subject}成绩需在0-100之间，请重新输入！")
            except ValueError:
                print(f"{subject}成绩必须是数字，请重新输入！")
    
    china_score = get_valid_score("语文")
    math_score = get_valid_score("数学")
    english_score = get_valid_score("英语")

    # 构造学生字典，新增总分、平均分字段
    total_score = china_score + math_score + english_score
    avg_score = total_score / 3
    student = {
        "name": name,
        "scores": {
            "语文": china_score,
            "数学": math_score,
            "英语": english_score
        },
        "total_score": total_score,  # 单个学生总分
        "avg_score": avg_score       # 单个学生平均分
    }

    students.append(student)
    print(f"✅ 学生【{name}】信息录入完成！")

def calc_student_avg():
    """计算并打印：①每个学生的总分/平均分 ②全体学生的科目平均分/总平均分"""
    if not students:
        print("⚠️ 暂无学生信息，请先录入！")
        return
    
    # 单个学生的总分、平均分
    print("\n===== 单个学生成绩详情 =====")
    for stu in students:
        print(f"姓名：{stu['name']} | 总分：{stu['total_score']} | 平均分：{stu['avg_score']:.2f}")
        print(f"     语文：{stu['scores']['语文']} | 数学：{stu['scores']['数学']} | 英语：{stu['scores']['英语']}\n")
    
    # 全体学生的科目平均分、总平均分
    total_all = sum(stu["total_score"] for stu in students)
    china_total = sum(stu["scores"]["语文"] for stu in students)
    math_total = sum(stu["scores"]["数学"] for stu in students)
    english_total = sum(stu["scores"]["英语"] for stu in students)
    
    stu_count = len(students)
    total_avg = total_all / stu_count
    china_avg = china_total / stu_count
    math_avg = math_total / stu_count
    english_avg = english_total / stu_count

    print("===== 全体学生成绩统计 =====")
    print(f"总平均分：{total_avg:.2f} | 语文平均分：{china_avg:.2f} | 数学平均分：{math_avg:.2f} | 英语平均分：{english_avg:.2f}")

def filter_passed_students():
    """筛选平均分≥60的学生（每次筛选重新计算，避免重复）"""
    if not students:
        print("⚠️ 暂无学生信息，请先录入！")
        return
    
    passed_students = [stu["name"] for stu in students if stu["avg_score"] >= 60]
    print("\n===== 平均分≥60分的学生名单 =====")
    if passed_students:
        print("、".join(passed_students))
    else:
        print("暂无学生达标")

def print_all_students():
    """格式化打印所有学生完整信息"""
    if not students:
        print("⚠️ 暂无学生信息，请先录入！")
        return
    
    print("\n===== 所有学生信息 =====")
    for idx, stu in enumerate(students, 1):
        print(f"[{idx}] 姓名：{stu['name']}")
        print(f"    语文：{stu['scores']['语文']} | 数学：{stu['scores']['数学']} | 英语：{stu['scores']['英语']}")
        print(f"    总分：{stu['total_score']} | 平均分：{stu['avg_score']:.2f}\n")

# 主程序入口
def main():
    menu = """
===== 学生成绩管理系统 =====
1. 录入单个学生信息
2. 批量录入学生信息
3. 计算平均分（单个+全体）
4. 筛选平均分≥60分的学生
5. 打印所有学生信息
其他数字. 退出系统
==========================
请输入操作序号："""
    
    while True:
        try:
            choice = int(input(menu))
        except ValueError:
            print("❌ 输入无效，请输入数字序号！")
            continue
        
        if choice == 1:
            add_student()
        elif choice == 2:
            print("\n===== 批量录入学生信息 =====")
            while True:
                add_student()
                # 批量录入的继续确认（仅接受1/0）
                while True:
                    try:
                        continue_choice = int(input("是否继续录入？【1=继续 | 0=停止】："))
                        if continue_choice in (0, 1):
                            break
                        else:
                            print("❌ 仅支持输入1或0，请重新选择！")
                    except ValueError:
                        print("❌ 输入无效，请输入数字1或0！")
                if continue_choice == 0:
                    print("✅ 批量录入结束！")
                    break
        elif choice == 3:
            calc_student_avg()
        elif choice == 4:
            filter_passed_students()
        elif choice == 5:
            print_all_students()
        else:
            print("👋 退出系统，感谢使用！")
            break

if __name__ == "__main__":
    main()