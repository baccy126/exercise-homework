# 3. 写出下列程序运行结果:
#     (1)
input_number = 8
random_number = 8
if input_number == random_number:
    print("猜对了")
else:
    print("猜错了")

# 答: 执行结果是"猜对了"


# (2)
num = 12
if num > 3:
    print("⼤于3")
elif num > 5:
    print("⼤于5")
elif num > 10:
    print("⼤于10")
elif num > 15:
    print("⼤于10")

# 答: 执行结果是"大于3"

# (3)
str_value = " "
new_str = str_value if str_value else "empty"
print(new_str)
# 答: 执行结果是 "empty", 回答错误, 引号里面有空格. 执行结果应该是一个空格.

# 4. 根据需求写出程序
#     (1) 电梯设置规定：
#             如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
#         步骤:
#             终端中获取人数/总重量
#             显示电梯正常运行
#                 电梯超载
#
# 答:
if int(input("请输入人数:")) <= 10 and float(input("请输入总重量(千克):")) <= 1000:
    print("电梯正常运行")
else:
    print("电梯超载")

# (2) 根据年龄，输出对应的人生阶段。
#             年龄       ⼈⽣阶段
#             0-6 岁      童年
#             7-17 岁     少年
#             18-40 岁    ⻘年
#             41-65 岁    中年
#             65 岁之后    ⽼年
#         步骤:
#             终端中获取年龄
#             显示人生阶段
# 答:
get_age = int(input("请输入您的年龄:"))
if get_age <= 6:
    print("你还处于童年期.")
elif get_age <= 17:
    print("你处于少年期.")
elif get_age <= 40:
    print("你处于青年期.")
elif get_age <= 65:
    print("你处于中年期.")
else:
    print("你处于老年期.")

#
#     (3) 如果是vip客户,消费小于等于500,享受85折
#                     消费大于500,享受8折
#         如果不是vip客户,消费大于等于800,享受9折
#                       消费小于800,原价
#         在终端中输入账户类型,消费金额,计算折扣.
#         循环计算折扣,直到账户输入空字符串结束
#
# 答:
while True:
    account_type = input("请输入账户类型:")
    if account_type == "":
        break
    total_consumption = float(input("请输入消费金额:"))
    if account_type == "vip":
        if total_consumption <= 500:
            print("享受85折")
        else:
            print("享受8折")
    else:
        if total_consumption >= 800:
            print("享受9折")
        else:
            print("原价")
print("程序结束.")

#     (4) 梯形面积： （上底 + 下底) * 高  / 2
#         在终端中获取上底/下底/高
#         打印面积
#
# 答:
upper_length = float(input("请输入上底长:"))
bottom_length = float(input("请输入下底长:"))
height = float(input("请输入高度:"))
print((upper_length + bottom_length) * height / 2)


# 因为自学过一遍第一阶段, 所以碰到这道题, 想用面向对象的思想解一遍:
class GraphicManager:
    def __init__(self):
        self.graphics = []

    def add_graphic(self, graphic):
        self.graphics.append(graphic)

    def get_total_area(self):
        result = 0
        for i in self.graphics:
            result += i.calculate()
        return result


class Graphic:
    def __init__(self):
        raise NotImplementedError()

    def calculate(self):
        pass


# ---------------隔离---------------------
class TrapezoidAre(Graphic):
    def __init__(self, upper_length, bottom_length, height):
        self.upper_length = upper_length
        self.bottom_length = bottom_length
        self.height = height

    def calculate(self):
        return (self.upper_length + self.bottom_length) * self.height / 2


if __name__ == '__main__':
    t01 = TrapezoidAre(1, 4, 1)
    g01 = GraphicManager()
    g01.add_graphic(t01)
    print(g01.get_total_area())

# (5)
# 小泽老师很不幸, 买了一箱有虫子(1只)的苹果
# 虫子吃完一个苹果再吃另外一个苹果
# 在终端中输入苹果数量(个), 虫子吃苹果的速度(小时 / 个), 经过时间(小时)
# 请打印没有被虫子吃过的苹果数量（整数, 最小也是0）
# 答:
number_of_apple = int(input("请输入苹果数量:"))
speed_of_eating = float(input("请输入虫子吃苹果的速度(小时/个):"))
duration = int(input("请输入经过时间(小时):"))
count = 0
while count < duration:
    number_of_apple -= 1 / speed_of_eating
    if number_of_apple == 0:
        print("苹果都被虫子吃完啦")
        break
    count += 1
print("小泽老师还剩" + str(number_of_apple) + "个苹果.")

# (6)
# while 循环累加练习
#     使用while循环累加下列数字：0 + 1 + 2 + 3
k = 0
result = 0
while k < 4:
    result = (k + 1) * k / 2
    k += 1
print(result)
#     使用while循环累加下列数字：2 + 3 + 4 + 5 + 6
k = 0
result = 0
while k < 7:
    result = (k + 1) * k / 2 - 1
    k += 1
print(result)
#     使用while循环累加下列数字：1 + 3 + 5 + 7
# 4**2
k = 0
result = 0
while k < 4:
    result = (k + 1) ** 2
    k += 1
print(result)
#     使用while循环累加下列数字：8 + 7 + 6 + 5 + 4
k = 0
result = 0
while k < 9:
    result = (k + 1) * k / 2 - 6
    k += 1
print(result)
#     使用while循环累加下列数字：-1 + -2 + -3 + -4 + -5
k = 0
result = 0
while k < 6:
    result = -(k + 1) * k / 2
    k += 1
print(result)
