import os
filename = 'student.txt'
def insert():  # 录入
    student_list = []
    while True:
        id1 = input("请输入ID（如1001）：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩"))
            python = int(input("请输入python成绩"))
            java = int(input("请输入java成绩"))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue
        # 将录入的学生信息保存到字典上
        student = {"id": id1, "name": name, "english": english, "python": python, "java": java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input("是否继续添加Y/N\n")
        if answer == 'Y':
            continue
        else:
            break

    # 调用save函数
    save(student_list)
    print("学生信息录入完毕！")


def save(lst):  # 保存到txt文本
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    while True:
        student_id = input("请输入要删除学生的id：")
        if student_id != '':
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, "r", encoding='UTF-8') as file:  # 打开文件
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否被删除
            if student_old:
                with open(filename, 'w', encoding='utf-8'):
                    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def main():
    while True:
        menu()
        choice = int(input("请选择"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出系统吗？y/n")
                if answer == 'y' or answer == 'Y':
                    print("谢谢您的使用")
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print("========================学生管理系统=========================")
    print("------------------------功能菜单----------------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出")
    print("----------------------------------------------------")


if __name__ == '__main__':
    main()
