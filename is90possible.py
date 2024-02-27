import random

summon_stack = 0
no_chance = 99.4
yes_chance = 0.6
list_of_summonstack = []
#내가 원하는 5성 뽑기
while True :
    if summon_stack <= 72 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star5[0] == 1 : 
            list_of_summonstack.append(summon_stack)
            summon_stack = 0
            no_chance = 99.4
            yes_chance = 0.6
    elif summon_stack >= 73 and summon_stack <= 88:
        no_chance = 99.4 - 6*(summon_stack - 72)
        yes_chance = 0.6 + 6*(summon_stack - 72)
        weights = [no_chance, yes_chance]
        population = [0,1]
        star5 = random.choices([0,1], weights)
        summon_stack += 1
        if star5[0] == 1 : 

            list_of_summonstack.append(summon_stack)
            summon_stack = 0
            no_chance = 99.4
            yes_chance = 0.6  
    elif summon_stack == 89 :
        summon_stack += 1
        list_of_summonstack.append(summon_stack)
        no_chance = 99.4
        yes_chance = 0.6
        if summon_stack == 90 :
            print("90!")
            break
        