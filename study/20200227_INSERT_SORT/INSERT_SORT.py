import random
import time
start = time.time()
data_list = random.sample(range(100), 50)
print(data_list)
'''
삽입정렬 로직
핵심: 1) 비교후 작은 값을 임시저장
     2) 저장 후 앞에 있는 값과 비교 작은 값의 순서를 저장
     3) 순서가 저장된 위치로 임시저장값을 삽입 
'''
def insert_sort(data):
    for i in range(0, len(data)-1, 1):
        if (data[i] > data[i+1]):
            temp = data[i+1]
            data.remove(data[i+1])
            minIndex = 0
            for j in range(i+1, 0, -1):
                if data[j-1] > temp:
                    minIndex = j-1
            data.insert(minIndex, temp)
    return data

print(insert_sort(data_list))
print("time :", time.time() - start)