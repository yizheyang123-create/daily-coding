"""
Python 字典（dict）进阶练习
2026-07-01
- 字典推导式
- defaultdict 默认值
- 合并字典（| 操作符）
- 字典解包
"""

from collections import defaultdict

# ======== 1. 字典推导式 ========
print("=" * 50)
print("1. 字典推导式")
print("=" * 50)

# 生成平方表
squares = {x: x**2 for x in range(1, 11)}
print(f"1~10 平方表: {squares}")

# 过滤：只保留偶数
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数的平方:   {even_squares}")

# key-value 互换
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"键值互换:     {swapped}")

# ======== 2. defaultdict 默认值 ========
print("\n" + "=" * 50)
print("2. defaultdict 默认值")
print("=" * 50)

# 统计单词出现次数
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = defaultdict(int)
for w in words:
    word_count[w] += 1
print(f"单词计数:     {dict(word_count)}")

# 按首字母分组
fruits = ["apple", "avocado", "banana", "blueberry", "cherry", "coconut"]
grouped = defaultdict(list)
for f in fruits:
    grouped[f[0]].append(f)
print(f"首字母分组:   {dict(grouped)}")

# ======== 3. 合并字典 (Python 3.9+) ========
print("\n" + "=" * 50)
print("3. 合并字典 | 操作符")
print("=" * 50)

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "Beijing", "age": 26}  # age 会覆盖

merged = dict1 | dict2
print(f"dict1:         {dict1}")
print(f"dict2:         {dict2}")
print(f"合并结果:      {merged}")

# ======== 4. get() 安全取值 ========
print("\n" + "=" * 50)
print("4. get() 安全取值")
print("=" * 50)

student = {"name": "小明", "score": 85}
print(f"姓名:   {student.get('name', '未知')}")
print(f"年龄:   {student.get('age', '未设置')}")  # 键不存在，返回默认值
print(f"分数:   {student.get('score', 0)}")

# ======== 5. 实际应用：字典作为小型数据库 ========
print("\n" + "=" * 50)
print("5. 学生信息查询系统")
print("=" * 50)

students = {
    1001: {"name": "张三", "score": 92, "grade": "A"},
    1002: {"name": "李四", "score": 78, "grade": "C"},
    1003: {"name": "王五", "score": 85, "grade": "B"},
    1004: {"name": "赵六", "score": 95, "grade": "A"},
    1005: {"name": "孙七", "score": 60, "grade": "D"},
}


def query_student(sid):
    """查询学生信息，安全处理不存在的学号"""
    info = students.get(sid)
    if info is None:
        return f"学号 {sid} 不存在"
    return f"{info['name']} - 成绩: {info['score']} - 等级: {info['grade']}"


def top_students(n=3):
    """返回成绩前 n 名的学生"""
    sorted_students = sorted(students.items(), key=lambda x: x[1]["score"], reverse=True)
    return {sid: info for sid, info in sorted_students[:n]}


# 测试查询
print(query_student(1001))
print(query_student(1003))
print(query_student(1999))  # 不存在的学号

# 成绩排名
print(f"\n成绩前3名: {top_students(3)}")

# 按等级分组
grade_groups = defaultdict(list)
for sid, info in students.items():
    grade_groups[info["grade"]].append(info["name"])
print(f"按等级分组: {dict(grade_groups)}")
