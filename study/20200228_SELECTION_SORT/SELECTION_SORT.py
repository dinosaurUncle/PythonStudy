import random
import time
start = time.time()
'''
선택정렬 로직
핵심: 1) 전체 비교후 가장 작은 값을 구하는 로직
     2) 구한 작은 값을 제외하고 맨 앞으로 배치
     2) 해당 순서를 제외하고 나머지를 반복하는 로직
'''
data_list = random.sample(range(100), 50)
for j in range(0, len(data_list), 1):
    min = 0
    for i in range(j, len(data_list), 1):
        if i == j :
            min = data_list[i]
        else :
            if min > data_list[i]:
                min = data_list[i]
    data_list.remove(min)
    data_list.insert(j, min)
print(data_list)
print("time :", time.time() - start)