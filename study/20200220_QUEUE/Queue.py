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

Enqueue -> put 메소드
Dequeue -> get 메소드
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