import random
import numpy as np
import matplotlib.pyplot as plt

n = 100000
summon_stack = 0
total_stack = 0
no_chance = 94.9
yes_chance = 5.1
list_of_howmuch_bannercharacter_cost = [] 
y_linear = []
x_linear = []
check_alwayscharcter = 1 # 0이면 픽뚫당한상태 1이면 아직 50% 확률
# 픽업 배너 5성 뽑기
while len(list_of_howmuch_bannercharacter_cost) <= 0:
    if summon_stack <= 7 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
        weights = [no_chance, yes_chance]
        star4 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star4[0] == 1 : 
            if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1,2,3], weights=[(50 + (3/37)) / 3, (50 + (3/37)) / 3, (50 + (3/37)) / 3, 50 - (3/37)])
                if fifty_fifty[0] == 0 : #내가 원하는 4성 캐릭터
                    check_alwayscharcter = 1
                    list_of_howmuch_bannercharacter_cost.append(summon_stack)
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1         #고치기
                    
                elif fifty_fifty[0] == 3 :
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : #4성 배너에서는 나왔지만 내가 원하는건 못얻음
                    check_alwayscharcter = 1
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
            elif check_alwayscharcter == 0 :
                check_alwayscharcter = 1
                total_stack = total_stack + summon_stack
                fifty_fifty = random.choices([0,1,2], weights=[100/3, 100/3, 100/3])
                if fifty_fifty[0] == 0  : #내가 원하는 4성 캐릭
                    list_of_howmuch_bannercharacter_cost.append(total_stack)
                    total_stack = 0
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : 
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
    if summon_stack == 8 :
        no_chance = 43.9
        yes_chance = 56.1
        weights = [no_chance, yes_chance]
        star4 = random.choices([0,1], weights)
        summon_stack += 1
        if star4[0] == 1 : 
            if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1,2,3], weights=[(50 + (3/37)) / 3, (50 + (3/37)) / 3, (50 + (3/37)) / 3, 50 - (3/37)])
                if fifty_fifty[0] == 0 : #내가 원하는 4성 캐릭터
                    check_alwayscharcter = 1
                    list_of_howmuch_bannercharacter_cost.append(summon_stack)
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1         #고치기
                    
                elif fifty_fifty[0] == 3 :
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : #4성 배너에서는 나왔지만 내가 원하는건 못얻음
                    check_alwayscharcter = 1
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
            elif check_alwayscharcter == 0 :
                check_alwayscharcter = 1
                total_stack = total_stack + summon_stack
                fifty_fifty = random.choices([0,1,2], weights=[100/3, 100/3, 100/3])
                if fifty_fifty[0] == 0  : #내가 원하는 4성 캐릭
                    list_of_howmuch_bannercharacter_cost.append(total_stack)
                    total_stack = 0
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : 
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
    if summon_stack == 9 :
        summon_stack += 1
        if star4[0] == 1 : 
            if check_alwayscharcter == 1 :
                fifty_fifty = random.choices([0,1,2,3], weights=[(50 + (3/37)) / 3, (50 + (3/37)) / 3, (50 + (3/37)) / 3, 50 - (3/37)])
                if fifty_fifty[0] == 0 : #내가 원하는 4성 캐릭터
                    check_alwayscharcter = 1
                    list_of_howmuch_bannercharacter_cost.append(summon_stack)
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1         #고치기
                    
                elif fifty_fifty[0] == 3 :
                    check_alwayscharcter = 0
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : #4성 배너에서는 나왔지만 내가 원하는건 못얻음
                    check_alwayscharcter = 1
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
            elif check_alwayscharcter == 0 :
                check_alwayscharcter = 1
                total_stack = total_stack + summon_stack
                fifty_fifty = random.choices([0,1,2], weights=[100/3, 100/3, 100/3])
                if fifty_fifty[0] == 0  : #내가 원하는 4성 캐릭
                    list_of_howmuch_bannercharacter_cost.append(total_stack)
                    total_stack = 0
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
                else : 
                    total_stack = total_stack + summon_stack
                    summon_stack = 0
                    no_chance = 94.9
                    yes_chance = 5.1
                    
print(list_of_howmuch_bannercharacter_cost)
def Average(list) : 
    return sum(list) / len(list)
# print("평균 뽑기 횟수 : " + str(Average(list_of_howmuch_bannercharacter_cost)) + "평균 소모 원석 : " + str(160 * Average(list_of_howmuch_bannercharacter_cost)))

print("원하는 4성 캐릭 나옴/전체경우 : " + str((len(list_of_howmuch_bannercharacter_cost)) / n))


for s in range(200) : 
    counts = list_of_howmuch_bannercharacter_cost.count(s+1)
    y_linear.append(counts)
    x_linear.append(s+1)
    s += 1
print("Done!")
plt.bar(x_linear, y_linear)
plt.show()



# import random
# import numpy as np
# import matplotlib.pyplot as plt

# n = 1000
# summon_stack = 0
# no_chance = 99.4
# yes_chance = 0.6
# list_of_summonstack = []
# y_linear = []
# x_linear = []
# # 5성 뽑기
# for i in range(n) :
#     i += 1
#     while summon_stack <= 72 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
#         weights = [no_chance, yes_chance]
#         star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
#         summon_stack += 1
#         if star5[0] == 1 : 
#             list_of_summonstack.append(summon_stack)
#             summon_stack = 0
#             no_chance = 99.4
#             yes_chance = 0.6
#             break
#     while summon_stack >= 73 and summon_stack <= 88:
#         no_chance = 99.4 - 6*(summon_stack - 72)
#         yes_chance = 0.6 + 6*(summon_stack - 72)
#         weights = [no_chance, yes_chance]
#         population = [0,1]
#         star5 = random.choices([0,1], weights)
#         summon_stack += 1
#         if star5[0] == 1 : 
#             list_of_summonstack.append(summon_stack)
#             summon_stack = 0
#             no_chance = 99.4
#             yes_chance = 0.6    
#             break
#     while summon_stack == 89 :
#         summon_stack += 1
#         list_of_summonstack.append(summon_stack)
#         summon_stack = 0
#         no_chance = 99.4
#         yes_chance = 0.6
#         break
# print(list_of_summonstack)
# def Average(list) : 
#     return sum(list) / len(list)
# print("평균 뽑기 횟수 : " + str(Average(list_of_summonstack)) + "평균 소모 원석 : " + str(160 * Average(list_of_summonstack)))



# for s in range(180) : 
#     counts = list_of_summonstack.count(s+1)
#     y_linear.append(counts)
#     x_linear.append(s+1)
#     s += 1
# print("Done!")
# plt.bar(x_linear, y_linear)
# plt.show()