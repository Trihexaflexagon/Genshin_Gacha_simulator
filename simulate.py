import random
import tkinter

window = tkinter.Tk()
window.title("Genshin Gacha")
window.geometry("640x400")
window.resizable(False, False)
n = 1000
summon_stack = 0
no_chance = 99.4
yes_chance = 0.6
list_of_summonstack = []
# 5성 뽑기
for i in range(n) :
    i += 1
    while summon_stack <= 72 : #뽑기를 누르고 1스택이 올라감 --- 1번째 뽑기에선 0스택, 2번째 뽑기에선 1스택, 73번째 뽑기에선 72스택, 74번째에선 73스택
        weights = [no_chance, yes_chance]
        star5 = random.choices([0,1], weights) #1~73스택, 리스트 형태
        summon_stack += 1
        if star5[0] == 1 : 
            list_of_summonstack.append(summon_stack)
            summon_stack = 0
            no_chance = 99.4
            yes_chance = 0.6
            break
    while summon_stack >= 73 and summon_stack <= 88:
        no_chance = 99.4 - 6*(summon_stack - 73)
        yes_chance = 0.6 + 6*(summon_stack - 73)
        weights = [no_chance, yes_chance]
        population = [0,1]
        star5 = random.choices([0,1], weights)
        summon_stack += 1
        if star5[0] == 1 : 
            list_of_summonstack.append(summon_stack)
            summon_stack = 0
            no_chance = 99.4
            yes_chance = 0.6    
            break
    while summon_stack == 89 :
        summon_stack += 1
        list_of_summonstack.append(summon_stack)
        summon_stack = 0
        no_chance = 99.4
        yes_chance = 0.6
        break
print(len(list_of_summonstack))
def Average(list) : 
    return sum(list) / len(list)
print("평균 뽑기 횟수 : " + str(Average(list_of_summonstack)) + "평균 소모 원석 : " + str(160 * Average(list_of_summonstack)))



label = tkinter.Label(window, text = str(Average(list_of_summonstack)), width = 30, height = 20, relief = "solid")
label.pack()
window.mainloop()