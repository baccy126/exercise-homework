# 8. (选做)斐波那契数列：从第三项开始,每一项都等于前两项之和。
#         在终端中获取长度,创建斐波那契数列。
#         演示：
#             请输入斐波那契数列长度：8
#             [1, 1, 2, 3, 5, 8, 13, 21]
#         提示: 列表初始值: [1,1]
get_len=int(input("请输入斐波那契数列长度:"))
result_list=[1,1]
for i in range(2,get_len):
    fib=result_list[i-1]+result_list[i-2]
    result_list.append(fib)
print(result_list)