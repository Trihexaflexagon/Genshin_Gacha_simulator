import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000
summon_stack = 0
total_stack = 0
no_chance = 99.3
yes_chance = 0.7
list_of_howmuch_banner1weapon_what_I_want_cost = []
gods_orbit = 0
isbannerweapon = False
for i in range(n) :
    i += 1
    while summon_stack <= 61 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star5[0] == 1 : 
            if gods_orbit == 2 : 
                isbannerweapon = False
                total_stack = total_stack + summon_stack
                list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                summon_stack = 0
                total_stack = 0
                no_chance = 99.3
                yes_chance = 0.7
                gods_orbit = 0
            else : 
                if isbannerweapon == False : 
                    the5star = random.choices([0,1,2], weights=[37.5,37.5,25]) # 0이 픽뚫, 1이 banner1(내가 원하는거), 2가 banner2
                    if the5star[0] == 0 :
                        isbannerweapon == True
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                    if the5star[0] == 1 :
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 : 
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                elif isbannerweapon == True : 
                    the5star = random.choices([1,2], weights=[50,50]) # 1이 banner1(내가 원하는거), 2가 banner2 
                    if the5star[0] == 1 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
    while summon_stack >= 62 and summon_stack <= 75:
        no_chance = 99.3 - 7*(summon_stack - 61)
        yes_chance = 0.7 + 7*(summon_stack - 61)
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights)
        summon_stack += 1
        if star5[0] == 1 : 
            if gods_orbit == 2 : 
                isbannerweapon = False
                total_stack = total_stack + summon_stack
                list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                summon_stack = 0
                total_stack = 0
                no_chance = 99.3
                yes_chance = 0.7
                gods_orbit = 0
            else : 
                if isbannerweapon == False : 
                    the5star = random.choices([0,1,2], weights=[37.5,37.5,25]) # 0이 픽뚫, 1이 banner1(내가 원하는거), 2가 banner2
                    if the5star[0] == 0 :
                        isbannerweapon == True
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                    if the5star[0] == 1 :
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 : 
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                elif isbannerweapon == True : 
                    the5star = random.choices([1,2], weights=[50,50]) # 1이 banner1(내가 원하는거), 2가 banner2 
                    if the5star[0] == 1 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
    while summon_stack == 76 :
        weights = [0, 100]
        star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star5[0] == 1 : 
            if gods_orbit == 2 : 
                isbannerweapon = False
                total_stack = total_stack + summon_stack
                list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                summon_stack = 0
                total_stack = 0
                no_chance = 99.3
                yes_chance = 0.7
                gods_orbit = 0
            else : 
                if isbannerweapon == False : 
                    the5star = random.choices([0,1,2], weights=[37.5,37.5,25]) # 0이 픽뚫, 1이 banner1(내가 원하는거), 2가 banner2
                    if the5star[0] == 0 :
                        isbannerweapon == True
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                    if the5star[0] == 1 :
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 : 
                        isbannerweapon == False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
                elif isbannerweapon == True : 
                    the5star = random.choices([1,2], weights=[50,50]) # 1이 banner1(내가 원하는거), 2가 banner2 
                    if the5star[0] == 1 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        list_of_howmuch_banner1weapon_what_I_want_cost.append(total_stack)
                        summon_stack = 0
                        total_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit = 0
                        break
                    elif the5star[0] == 2 :
                        isbannerweapon = False
                        total_stack = total_stack + summon_stack
                        summon_stack = 0
                        no_chance = 99.3
                        yes_chance = 0.7
                        gods_orbit += 1
                        break
# print(list_of_howmuch_banner1weapon_what_I_want_cost)
# def Average(list) : 
#     return sum(list) / len(list)
# print("평균 뽑기 횟수 : " + str(Average(list_of_howmuch_banner1weapon_what_I_want_cost)) + "평균 소모 원석 : " + str(160 * Average(list_of_howmuch_banner1weapon_what_I_want_cost)))

# print("원하는거 5성 나옴/전체경우 : " + str((len(list_of_howmuch_banner1weapon_what_I_want_cost)) / n))

x_linear = []
y_linear = []
for s in range(231) : 
    counts = list_of_howmuch_banner1weapon_what_I_want_cost.count(s+1)
    y_linear.append(counts)
    x_linear.append(s+1)
    s += 1
print("Done!")
plt.bar(x_linear, y_linear)
plt.show()