print("-"*20,"唐省与白骨精","-"*20)

print("选择身份:")
print("\t1.唐僧")
print("\t2.白骨精")

player = int(input("请选择:"))
print("-"*40)
if player == 1 :
    print("\t你选择1，以唐生做游戏")
elif player == 2 :
    print("\t不是白骨精，是唐生")
else:
    print("\t输入有误，为唐生")

#进入游戏


#创建变量保存玩家生命值与攻击力

player_life = 2
player_attack = 2

boss_life = 10
boss_attack = 10

#显示玩家的信息(攻击力与生命值)
print(f"你的攻击力{player_attack},生命之{player_life}")


while True:
    print("请选择操作:")
    print("1.练级")
    print("2.打boss")
    print("3.退出")
    game_choose = input("选择操作:")
    if game_choose == '1':
        player_attack+=2
        player_life+=2
    elif game_choose == '2':
        boss_life -= player_attack
        if boss_life <= 0:
            print("玩家胜利")
            break
        player_life -= boss_attack
        if player_life <= 0:
            print("boss胜利")
            break
    else:
        break
    #显示玩家的信息(攻击力与生命值)
    print(f"你的攻击力{player_attack},生命之{player_life}")