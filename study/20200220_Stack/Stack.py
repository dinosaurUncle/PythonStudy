'''
 자료구조: 스택 (Stack)
 데이터를 제한적으로 접근할 수 있는 구조 -> 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조 -> LIFO(Last-In, First-Out)
 <-> Queue

 알아둘 용어
 push: 데이터를 스택에 넣기
 pop: 데이터를 스택에서 꺼내기

 스택 구조와 프로세스 스택
 스택 구조는 프로세스 실행 구조의 가장 기본
 -> 함수 호출시 프로세스 실행 구조를 스택과 비교해서 이해 필요

 자료 구조 스택의 장단점
 장점
    구조가 단순해서, 구현이 쉽다.
    데이터 저장/읽기 속도가 빠르다.
 단점
    데이터 최대 갯수를 미리 정해야 한다.(파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능함)
    저장 공간의 낭비가 발생할 수 있음(미리 최대 갯수만큼 저장 공간을 확보해야 함)
'''

## Stack 실습(list 기능에서 stack이 기능 제공)
data_stack = list()

data_stack.append('종훈')
data_stack.append('흥민')
data_stack.append('의조')
data_stack.append('승우')
print('data_stack의 크기: ', len(data_stack))

print('stack의 데이터: ', data_stack.pop())
print('stack의 데이터: ', data_stack.pop())
print('stack의 데이터: ', data_stack.pop())

print('data_stack의 크기: ', len(data_stack))
