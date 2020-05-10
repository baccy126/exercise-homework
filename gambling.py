# 7. 赌大小游戏
#     玩家的身家初始10000，实现下列效果：
#         少侠请下注: 30000
#         超出了你的身家，请重新投注。
#         少侠请下注: 8000
#         你摇出了5点,庄家摇出了3点
#         恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
#         少侠请下注: 18000
#         你摇出了6点,庄家摇出了6点
#         打平了，少侠，在来一局？
#         少侠请下注: 18000
#         你摇出了4点,庄家摇出了6点
#         少侠,你输了，身家还剩 0
#         哈哈哈，少侠你已经破产，无资格进行游戏
import random
player_account=10000
while player_account>0:
    bet=input("少侠请下注:")
    if bet=="":
        break
    elif int(bet)>player_account:
        print("超出了你的身家，请重新投注。")
    else:
        player_number=random.randint(1,6)
        system_number=random.randint(1,6)
        print(f"你摇出了{player_number}点,庄家摇出了{system_number}点.")
        if player_number>system_number:
            player_account+=int(bet)
            print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d"%player_account)
        elif player_number<system_number:
            player_account-=int(bet)
            print("少侠,你输了，身家还剩%d" % player_account)
        else:
            print("打平了，少侠，在来一局？")
else:
    print("哈哈哈，少侠你已经破产，无资格进行游戏.")