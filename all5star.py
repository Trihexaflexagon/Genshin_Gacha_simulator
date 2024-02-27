import random
import numpy as np
import matplotlib.pyplot as plt
from statistics import mode
#위에 4줄 몰라도 됨(아래 코드를 실행하기 위해 필요)

#for 코드 : 내가 지정한 횟수 만큼 반복
#while 코드 : 조건이 충족될때 계속 반복 실행 (조건이 충족되지 않으면 실행 X, 다음 코드로 넘어감)
#리스트 : 여러 변수를 저장할수 있는 변수들의 집합 (예를 들어 변수가 책이라면 리스트는 책꽂이)

n = 10000000 # 총 반복횟수 설정
summon_stack = 0 #뽑기 스택
no_chance = 99.4 #안뽑히는 확률
yes_chance = 0.6 #뽑히는 확률
list_of_summonstack = [] #뽑기 횟수들을 저장하는 리스트
y_linear = [] #그래프 그릴때 필요
x_linear = [] #그래프 그릴때 필요


#5성 뽑기
for i in range(n) : #n회만큼 반복
    i += 1 #n회만큼 반복하는데 필요한 코드
    while summon_stack <= 72 : #1개씩 뽑는걸 반복 --- ex) 1번째 뽑기에선 뽑기전에 0스택, 74번째에선 뽑기전에 73스택   ---> 아래의 코드를 73스택이 되기 전까지 실행 ---> 최대 73번 뽑음
        weights = [no_chance, yes_chance] #뽑기에 확률을 적용해 가중치를 줌
        star5 = random.choices([0,1], weights) #1~73스택, 랜덤으로 뽑기. 안뽑혔으면 변수에 0 저장, 뽑혔으면 변수에 1 저장. (리스트 형태)
        summon_stack += 1 #한번 뽑았으니 스택에 1 추가
        if star5[0] == 1 : #만약에 변수에 1이 저장됐으면 (5성이 뽑혔으면)
            list_of_summonstack.append(summon_stack) # 13번 줄에 있던 변수에 스택을 저장시킴
            summon_stack = 0 # 다음 뽑기를 위해 스택 초기화
            no_chance = 99.4 # 다음 뽑기를 위해 확률 초기화
            yes_chance = 0.6 # 다음 뽑기를 위해 확률 초기화
            break #while 코드 탈출(처음부터 뽑기 시작)
    while summon_stack >= 73 and summon_stack <= 88: # 73번 뽑기에서도 안나왔을시 74번째 뽑기부터 89번째 뽑기까지 실행
        no_chance = 99.4 - 6*(summon_stack - 72) # 안뽑힐확률이 6%p만큼 감소하기때문에 확률을 0.6 - 6*(스택-72)로 설정
        yes_chance = 0.6 + 6*(summon_stack - 72) # 뽑힐확률이 6%p만큼 증가하기때문에 확률을 0.6 + 6*(스택-72)로 설정
        weights = [no_chance, yes_chance] #뽑기에 확률을 적용해 가중치를 줌
        star5 = random.choices([0,1], weights) #랜덤으로 뽑기. 안뽑혔으면 변수에 0 저장, 뽑혔으면 변수에 1 저장.
        summon_stack += 1 #한번 뽑았으니 스택에 1 추가
        if star5[0] == 1 : #만약에 변수에 1이 저장됐으면
            list_of_summonstack.append(summon_stack) # 13번 줄에 있던 변수에 스택을 저장시킴
            summon_stack = 0 # 다음 뽑기를 위해 스택 초기화
            no_chance = 99.4 # 다음 뽑기를 위해 확률 초기화
            yes_chance = 0.6 # 다음 뽑기를 위해 확률 초기화   
            break #while 코드 탈출(처음부터 뽑기 시작)
    while summon_stack == 89 : #89스택일때 즉 ---> 90번째 뽑기 (무조건 5성 확정)
        summon_stack += 1 #한번 뽑았으니 스택에 1 추가
        list_of_summonstack.append(summon_stack) # 13번 줄에 있던 변수에 스택을 저장시킴
        summon_stack = 0 # 다음 뽑기를 위해 스택 초기화
        no_chance = 99.4 # 다음 뽑기를 위해 확률 초기화
        yes_chance = 0.6 # 다음 뽑기를 위해 확률 초기화
        break #while 코드 탈출(처음부터 뽑기 시작)
print(list_of_summonstack) #13번 변수에 저장된 값들을 모두 출력
def Average(list) : #평균값 구해줌
    return sum(list) / len(list)
print("평균 뽑기 횟수 : " + str(Average(list_of_summonstack)) + "평균 소모 원석 : " + str(160 * Average(list_of_summonstack))) #평균 뽑기 횟수랑 평균 소모 원석 출력



for s in range(90) : #그래프 생성
    counts = list_of_summonstack.count(s+1)
    y_linear.append(counts)
    x_linear.append(s+1)
    s += 1
print("최빈값 : " + str(mode(list_of_summonstack))) #최빈값 출력
print("Done!")
plt.bar(x_linear, y_linear) #그래프 나타나기
plt.show()