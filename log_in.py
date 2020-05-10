# 6. 模拟登录
# 如果账号的密码错误3次，提示锁定账户，效果如下：
#     请输入账号：qtx
#     请输入密码：1234
#     登录失败
#     你还剩余 2 次机会
#     请输入账号：Qtx
#     请输入密码：1234
#     登录失败
#     你还剩余 1 次机会
#     请输入账号：Qtx
#     请输入密码：123456
#     登录成功
count = 0
system_account = "Qtx"
system_code = "1234"
while count < 3:
    costomer_account = input("请输入账号名:")
    costomer_code = input("请输入密码:")
    if costomer_account == system_account and costomer_code == system_code:
        print("登陆成功.")
        break
    else:
        count += 1
        print("登陆失败.")
        print(f"你还剩余{3 - count}次登陆机会")
else:
    print("登陆失败.")
