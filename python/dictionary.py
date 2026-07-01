"""
简易英汉词典查询器 📖
2026-07-01
功能：查单词、添加单词、查看所有单词
"""

import sys
from collections import defaultdict

# 内置词典数据
dictionary = {
    "apple": "苹果",
    "banana": "香蕉",
    "cat": "猫",
    "dog": "狗",
    "elephant": "大象",
    "fish": "鱼",
    "good": "好的",
    "hello": "你好",
    "internet": "互联网",
    "java": "Java 编程语言",
    "key": "钥匙；关键",
    "love": "爱；喜欢",
    "money": "钱",
    "name": "名字",
    "open": "打开",
    "python": "蟒蛇；Python 编程语言",
    "queen": "女王",
    "run": "跑步；运行",
    "sun": "太阳",
    "tree": "树",
    "umbrella": "雨伞",
    "water": "水",
    "world": "世界",
}


def show_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("      📖 英汉词典 v1.0")
    print("=" * 40)
    print("  1. 🔍 查单词")
    print("  2. ➕ 添加单词")
    print("  3. 📋 查看所有单词")
    print("  4. 🟣 模糊搜索")
    print("  5. 🚪 退出")
    print("=" * 40)


def lookup_word(word):
    """查单词"""
    word = word.strip().lower()
    if not word:
        return "请输入单词！"
    meaning = dictionary.get(word)
    if meaning:
        return f"  {word}  →  {meaning}"
    return f"  未找到 '{word}'，试试用添加功能？"


def add_word(word, meaning):
    """添加单词"""
    word = word.strip().lower()
    meaning = meaning.strip()
    if not word or not meaning:
        return "单词和释义不能为空！"
    if word in dictionary:
        return f"  '{word}' 已存在（{dictionary[word]}），如需修改请先删除"
    dictionary[word] = meaning
    return f"  ✅ 已添加: {word}  →  {meaning}"


def show_all():
    """按字母排序显示所有单词"""
    if not dictionary:
        return "  词典还是空的，快添加一些单词吧！"
    lines = []
    # 按首字母分组
    grouped = defaultdict(list)
    for word, meaning in sorted(dictionary.items()):
        grouped[word[0].upper()].append(f"    {word:15s} → {meaning}")

    result = f"  共 {len(dictionary)} 个单词\n"
    for letter in sorted(grouped):
        result += f"\n  [{letter}]\n"
        result += "\n".join(grouped[letter])
    return result


def fuzzy_search(keyword):
    """模糊搜索：匹配包含关键字的单词或释义"""
    keyword = keyword.strip().lower()
    if not keyword:
        return "请输入搜索关键字！"
    results = []
    for word, meaning in sorted(dictionary.items()):
        if keyword in word or keyword in meaning:
            results.append(f"    {word:15s} → {meaning}")
    if not results:
        return f"  未找到包含 '{keyword}' 的单词或释义"
    return f"  找到 {len(results)} 个结果:\n" + "\n".join(results)


def main():
    print("🐍 欢迎使用英汉词典！（输入 q 随时返回菜单）")
    while True:
        show_menu()
        choice = input("\n请选择 [1-5]: ").strip()

        if choice == "1":
            while True:
                word = input("  输入单词 (q 返回): ").strip()
                if word.lower() == "q":
                    break
                print(lookup_word(word))

        elif choice == "2":
            while True:
                word = input("  输入英文单词 (q 返回): ").strip()
                if word.lower() == "q":
                    break
                meaning = input("  输入中文释义: ").strip()
                print(add_word(word, meaning))

        elif choice == "3":
            print(show_all())
            input("  按 Enter 返回菜单...")

        elif choice == "4":
            while True:
                keyword = input("  输入关键字 (q 返回): ").strip()
                if keyword.lower() == "q":
                    break
                print(fuzzy_search(keyword))

        elif choice == "5":
            print("  👋 再见！继续加油学英语！")
            sys.exit(0)
        else:
            print("  ⚠️ 请输入 1-5")


if __name__ == "__main__":
    main()
