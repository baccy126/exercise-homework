import random

red_ball_pool=[]
c=0
while c<6:
    red_ball=random.randint(1,33)
    if red_ball not in red_ball_pool:
        red_ball_pool.append(red_ball)
        c+=1
blue_ball=random.randint(1,16)
print(red_ball_pool)
print(blue_ball)

red_ball_list=[]
count=0
while count<6:
    get_red_ball=int(input("请输入红球号码:"))
    if get_red_ball in red_ball_list:
        print("号码已存在, 请重新输入.")
    elif get_red_ball not in range(1,34):
        print("号码超出范围, 请重新输入.")
    else:
        red_ball_list.append(get_red_ball)
        count+=1
get_blue_ball=int(input("请输入蓝球号码:"))
if get_blue_ball not in range(1,16):
        print("号码超出范围, 请重新输入.")
print(red_ball_list,get_blue_ball)
