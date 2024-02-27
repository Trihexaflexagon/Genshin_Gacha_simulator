import random
import numpy as np
import matplotlib.pyplot as plt
from statistics import mode

i = 0 #건드리지 말기
c6total_stack = 0
check_6times = 0
n = 1000000 #실행 횟수
summon_stack = 0
total_stack = 0
no_chance = 99.4
yes_chance = 0.6
list_of_howmuch_bannercharacter_cost = [] 
y_linear = []
x_linear = []
check_alwayscharcter = 1 # 0이면 픽뚫당한상태 1이면 아직 50% 확률
# 픽업 배너 5성 뽑기
while i < n :
    while summon_stack <= 72 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star5[0] == 1 : 
            if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1])
                if fifty_fifty[0] == 1 :
                    check_alwayscharcter = 1
                    c6total_stack = c6total_stack + summon_stack
                    check_6times += 1
                    if check_6times == 6 :
                        list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                        c6total_stack = 0
                        check_6times = 0
                        i += 1
                        break
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
                else : 
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
            elif check_alwayscharcter == 0 :
                check_alwayscharcter = 1
                total_stack = total_stack + summon_stack
                c6total_stack = c6total_stack + total_stack
                check_6times += 1
                if check_6times == 6 :
                    list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                    c6total_stack = 0
                    check_6times = 0
                    i += 1
                    break
                total_stack = 0
                summon_stack = 0
                no_chance = 99.4
                yes_chance = 0.6
                break
    while summon_stack >= 73 and summon_stack <= 88:
        no_chance = 99.4 - 6*(summon_stack - 72)
        yes_chance = 0.6 + 6*(summon_stack - 72)
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights)
        summon_stack += 1
        if star5[0] == 1 : 
            if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1])
                if fifty_fifty[0] == 1 :
                    check_alwayscharcter = 1
                    c6total_stack = c6total_stack + summon_stack
                    check_6times += 1
                    if check_6times == 6 :
                        list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                        c6total_stack = 0
                        check_6times = 0
                        i += 1
                        break
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
                else : 
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
            elif check_alwayscharcter == 0 :
                check_alwayscharcter = 1
                total_stack = total_stack + summon_stack
                c6total_stack = c6total_stack + total_stack
                check_6times += 1
                if check_6times == 6 :
                    list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                    c6total_stack = 0
                    check_6times = 0
                    i += 1
                    break
                total_stack = 0
                summon_stack = 0
                no_chance = 99.4
                yes_chance = 0.6
                break
    while summon_stack == 89 :
        summon_stack += 1
        if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1])
                if fifty_fifty[0] == 1 :
                    check_alwayscharcter = 1
                    c6total_stack = c6total_stack + summon_stack
                    check_6times += 1
                    if check_6times == 6 :
                        list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                        c6total_stack = 0
                        check_6times = 0
                        i += 1
                        break
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
                else : 
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 99.4
                    yes_chance = 0.6
                    break
        elif check_alwayscharcter == 0 :
            check_alwayscharcter = 1
            total_stack = total_stack + summon_stack
            c6total_stack = c6total_stack + total_stack
            check_6times += 1
            if check_6times == 6 :
                list_of_howmuch_bannercharacter_cost.append(c6total_stack)
                c6total_stack = 0
                check_6times = 0
                i += 1
                break
            total_stack = 0
            summon_stack = 0
            no_chance = 99.4
            yes_chance = 0.6
            break
print(list_of_howmuch_bannercharacter_cost)
def Average(list) : 
    return sum(list) / len(list)
print("평균 뽑기 횟수 : " + str(Average(list_of_howmuch_bannercharacter_cost)) + "평균 소모 원석 : " + str(160 * Average(list_of_howmuch_bannercharacter_cost)))


for s in range(1080) : 
    counts = list_of_howmuch_bannercharacter_cost.count(s+1)
    y_linear.append(counts)
    x_linear.append(s+1)
    s += 1
print("최빈값 : " + str(mode(list_of_howmuch_bannercharacter_cost)))
print("Done!")
plt.bar(x_linear, y_linear)
plt.show()