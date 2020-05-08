# 使用列表存储1970年到2050年之间所有闰年
list_result=[]
for i in range(1970,2051):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        list_result.append(i)
print(list_result)

list_result=[i for i in range(1970,2051) if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]
print(list_result)
