import random
import time
start = time.time()

data_list = random.sample(range(100), 50)
'''
버블정렬 로직
핵심 1) 자리수 계산
    2) 인접한 두 수의 크기 비교
    3) 자리 변경이 있는지 여부
'''

def bubble_sort(list):
    change = True
    while change:
        order = 1
        change = False
        while (len(list) - order) != 0:
            for i in range(order-1, len(list)-1, 1):
                if list[i] > list[i+1] :
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
                    change = True
            order = order+1
            if not change:
                break
    return list


def bubble_sort2(data):
    for index in range(len(data_list)):
        swap = 0
        for index2 in range(len(data_list) - 1 - index):
            if data_list[index2] > data_list[index2 + 1]:
                data_list[index2], data_list[index2 + 1] = data_list[index2 + 1], data_list[index2]
                swap += 1
        if swap == 0:
            break
    return data_list

print(bubble_sort(data_list))
print(bubble_sort2(data_list))
print("time :", time.time() - start)