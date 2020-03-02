'''
동적계획법(Dynamic Programming)

피보나치 수열
-> 계산하는 과정에서 중복이 발생

Memoization
계산한 값을 배열에 저장하고 필요할 때 가져온다

어떤 순환식을 계산할 때 배열 사용해서 값을 구하는 테크닉 Dynamic Programming
'''





## 실습 일반적인 피보나치 수열의 예
def normally_fibonacci_logic(num):
    if num == 1 or num == 2 :
        return 1
    else :
        return normally_fibonacci_logic(num-1) + normally_fibonacci_logic(num-2)
print(normally_fibonacci_logic(1))
print(normally_fibonacci_logic(2))
print(normally_fibonacci_logic(3))
print(normally_fibonacci_logic(4))
print(normally_fibonacci_logic(5))

'''
위와 같이 진행할 경우 이렇게 진행할 경우 
7값을 넣었을때  6과 5를 얻어야 하므로
6은 5와 4를 5는 3과 4를 얻어야 한다 이때만 봐도 벌써 4가 두번 중복된 것을 확인할 수 있다
이를 방지하고자 이미 4라는 값이 계산된 결과이므로 이를 저장하였다가 이 값이 필요할 때 불러서 쓴다
중복된 계산을 피하는 테크닉 memoization이다

'''
def memoization_fibonacci(num):
    tempList = memoization(num)
    return fibonacci(num, tempList)

def memoization(num):
    tempList = list()
    for i in range(num):
        tempList.insert(i, 0)
    return tempList

def fibonacci(num, tempList):
    if num == 1 or num == 2 :
        return 1
    elif tempList[num-1] > 0:
        return tempList[num-1]
    else :
        tempList[num-1] = fibonacci(num-1, tempList) + fibonacci(num-2, tempList)
        return tempList[num-1]

print(memoization_fibonacci(1))
print(memoization_fibonacci(2))
print(memoization_fibonacci(3))
print(memoization_fibonacci(4))
print(memoization_fibonacci(5))


'''
순서대로 값을 얻어서 결과값에 도달하는 방식
bottom-up 방식


'''
def bottomUP_fibonacci(num):
    tempList = list();
    tempList.insert(0, 1)
    tempList.insert(1, 1)
    for i in range(3, num+1):
        tempList.insert(i, 0)
    return b_fibonacci(num, tempList)

def b_fibonacci(num, tempList):
    if num == 1 or num == 2:
        return tempList[num-1]
    else:
        for i in range(3, num+1):
            tempList[i-1] = tempList[i-2] + tempList[i-3]
        return tempList[num-1]


print(bottomUP_fibonacci(10))