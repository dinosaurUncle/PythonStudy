'''
큐 (Queue)
줄을 서는 행위와 유사
가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조(FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식)
<-> 스택

알아둘 용어
Enqueue: 큐에 데이터를 넣는 기능
Dequeue: 큐에서 데이터를 꺼내는 기능

종류
Queue(): 가장 일반적인 큐 자료 구조
LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

구현시 사용 메소드
Enqueue -> put 메소드
Dequeue -> get 메소드
queue의 크기 확인시 qsize 메소드

사용되는 상황의 예
멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)
큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음

'''

## Queue 실습
import queue

data_queue = queue.Queue()

data_queue.put('종훈')
data_queue.put('흥민')
data_queue.put('의조')
data_queue.put('승우')

print('queue의 크기: ', data_queue.qsize())

print('queue의 데이터: ', data_queue.get())
print('queue의 데이터: ', data_queue.get())
print('queue의 데이터: ', data_queue.get())
print('queue의 크기: ', data_queue.qsize())

## LifeQue 실습

data_lifeQueue = queue.LifoQueue()

data_lifeQueue.put('종훈')
data_lifeQueue.put('흥민')
data_lifeQueue.put('의조')
data_lifeQueue.put('승우')

print('lifeQueue의 크기: ', data_lifeQueue.qsize())

print('lifeQueue의 데이터: ', data_lifeQueue.get())
print('lifeQueue의 데이터: ', data_lifeQueue.get())
print('lifeQueue의 데이터: ', data_lifeQueue.get())

print('lifeQueue의 크기: ', data_lifeQueue.qsize())

## PriorityQueue 실습

data_priorityQueue = queue.PriorityQueue();

data_priorityQueue.put((100, '종훈'))
data_priorityQueue.put((25, '흥민'))
data_priorityQueue.put((125, '의조'))
data_priorityQueue.put((40, '승우'))

print('priorityQueue의 크기: ', data_priorityQueue.qsize())

print('priorityQueue의 데이터: ', data_priorityQueue.get())
print('priorityQueue의 데이터: ', data_priorityQueue.get())
print('priorityQueue의 데이터: ', data_priorityQueue.get())


print('priorityQueue의 크기: ', data_priorityQueue.qsize())