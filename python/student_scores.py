
'''
学生成绩管理系统
用来存学生成绩的字典，格式：{“姓名”:分数}
'''
student={}
def add_student(name,score):
    # 添加学生和成绩
    student[name]=score#把名字和分数存进字典
    print(f"已添加学生：{name}，成绩:{score}")

def show_all():
    #显示所有学生成绩
    print("所有学生成绩：")
    for name,score in student.items():
        print(f"{name},{score}分")
    
def average():
    #计算平均分
    if len(student)==0:
        print("还没有学生数据")
        return
    total=sum(student.values())
    avg=total/len(student)
    print(f"平均分：{avg:.1f}分")
def top_student():
     #最高分学生
    if len(student)==0:
        print("还没有学生数据")
        return
    max_name=max(student,key=student.get)
    max_score=student[max_name]
    print(f"最高分：{max_name}，{max_score}")

'''运行演示'''
print("="*30)
print("学生成绩管理系统")
print("="*30)

add_student("张三",85)
add_student("李四",92)
add_student("王五",78)
add_student("赵六",95)

print()
show_all()

print()
average()

#print()
top_student()