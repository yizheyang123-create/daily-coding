# 列表操作练习

fruits = ["苹果", "香蕉", "橘子", "西瓜"]

# 遍历列表
print("水果列表：")
for fruit in fruits:
    print(f"  - {fruit}")

# 添加元素
fruits.append("葡萄")
print(f"\n添加后：{fruits}")

# 删除元素
fruits.remove("香蕉")
print(f"删除后：{fruits}")

# 切片
print(f"\n前两个水果：{fruits[:2]}")

# 排序
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(f"排序后：{numbers}")

# 列表长度
print(f"水果数量：{len(fruits)}")
