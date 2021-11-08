
# total = ['item_one', 'item_two', 'item_three',
#          'item_four', 'item_five']
# print(total)
#
# word = '这是一个字符串'
# sentence = "这是一个句子。"
# paragraph = "" "这是一个段落，" \
#             "可以多行组成" ""
# print(word)
# print(sentence)
# print(paragraph)
# # !/usr/bin/python3

# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始后的所有字符
# print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
#
# input("\n\n按下 enter 键后退出")

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# a, b, c = 1, 2, "12346"
# a = 1.2
# isinstance(a , int)

# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)     # a 和 b 的差集
#
# print(a | b)     # a 和 b 的并集
#
# print(a & b)     # a 和 b 的交集
#
# print(a ^ b)     # a 和 b 中不同时存在的元素

# list = ['a','b','c','d']
# newList = [123,'123']
# print(list)
#
# print(list[1:3])
# print(list[-1])
# print(list + newList)
# flag = False
#
# if flag :
#     print("yew It's work")
# else:
#     print("no You Not")
#
# '''
#     这也是注释么？
#     :param init
#
# '''

# print(2**24)
#
# print(15/7)
#
# print(15//7)

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5]
#
# if (a in list):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if (b not in list):
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
#
# # 修改变量 a 的值
# a = 2
# if (a in list):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")
# a = 10
#
# b = 10
#
# if (a is b):
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
#
# print(id(a))
#
# print(id(b))
#
# if (id(a) == id(b)):
#     print("2 - a 和 b 有相同的标识")
# else:
#     print("2 - a 和 b 没有相同的标识")
#
# # 修改变量 b 的值
# b = 30
# if (a is b):
#     print("3 - a 和 b 有相同的标识")
# else:
#     print("3 - a 和 b 没有相同的标识")
#
# if (a is not b):
#     print("4 - a 和 b 没有相同的标识")
# else:
#     print("4 - a 和 b 有相同的标识")

# a, b = 0, 1
# while b < 10000:
#     print(b, end=',')
#     a, b = b, a+b


# !/usr/bin/python3

# sites = ["Baidu", "Google", "Runoob", "Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         # print('执行 pass 块')
#     print('当前字母 :', letter)
#
# print("Good bye!")
# 0
# def change(a):
#     print(id(a))  # 指向的是同一个对象
#     a = 10
#     print(id(a))  # 一个新对象
#
#
# a = 1
# print(id(a))
# change(a)

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# a = 4
# b = 5
# print(max(a, b))

# def area(width, height):
#     return width * height
#
#
# def print_welcome(name):
#     print("Welcome", name)
#
#
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))


# !/usr/bin/python3

# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")

# !/usr/bin/python3

# 可写函数说明
# def printinfo(arg1, **vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
# ## 单星号是元组
# ## 双星号是字典
#
# # 调用printinfo 函数
# printinfo(70, a=60, b=50)

# sum = lambda var1,*var2:var1/var2[0]
#
# print(sum(1,2));

# name = input('please enter your name')
#
# print(name)

a = [66.251,333,333,1,1234.5]
a.append(12)

print(a)

L =  [1,12,123]
a.extend(L)
print(a)

print(a)

a.sort()

print(a)










