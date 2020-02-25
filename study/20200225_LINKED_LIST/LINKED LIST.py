'''
 자료구조: 리크드 리스트 (Linked list)
 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

 링크드 리스트 기본 구조와 용어
 노드(Node): 데이터 저장 단위(데이터값, 포인터)로 구성
 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

 링크드 리스트 장단점
 장점: 1) 미리 데이터 공간을 미리 할당하지 않아도 됨
 단점: 1) 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
      2) 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
      3) 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요



'''


'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

node = head


node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

while node.next:
    print(node.data)
    node = node.next
print(node.data)
'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else :
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)

nodeMgmt = NodeMgmt(0)

for i in range (1,10):
    nodeMgmt.add(i)

nodeMgmt.desc()

