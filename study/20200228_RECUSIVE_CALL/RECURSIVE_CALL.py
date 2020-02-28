'''
 재귀 용법(recursive call, 재귀 호출)
 함수 안에서 동일한 함수를 호출하는 형태
'''

## factorial 예제

def factorial(targetNum, indexNum=1, isInit = True):
    if isInit:
        if not indexNum == 1:
            return "잘못된 입력입니다"
        indexNum = 1
        isInit = False
        return indexNum * factorial(targetNum, indexNum + 1, isInit)
    else :
        if targetNum > indexNum:
            return indexNum * factorial(targetNum, indexNum + 1, isInit)
        else:
            return indexNum



print(factorial(10))