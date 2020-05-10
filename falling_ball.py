# 8. (选做)一个小球从100m高度落下,每次弹回原高度一半.
#    计算:
#     -- 总共弹起多少次?(最小弹起高度0.01m)
#     -- 全过程总共移动多少米?
#    提示:
#        数据/操作
#起始高度是100
height_start=100
# 最开始下落的100米加到这儿
total_distance=100
#计数器
count=0
#起跳高度大于0.01才是满足循环条件
while height_start/2>0.01:
    # 高度除以2得到下一次起始高度,
    height_start/=2
    # 总长是 = (起跳高度 + 下落高度) + 最开始下落的100米
    total_distance+=height_start*2
    count+=1
print(total_distance, count)