'''
 자료구조: 해쉬 테이블 (Hash Table)
 Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
 -> Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐

 알아둘 용어
 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수 <- GET 함수
 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간

 장점
    데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다.)
    해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
 단점
    일반적으로 저장공간이 좀더 많이 필요하다.
    여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
 주요 용도
    검색이 많이 필요한 경우
    저장, 삭제, 읽기가 빈번한 경우
    캐쉬 구현시 (중복 확인이 쉽기 때문)
'''

hash_table = list([0 for i in range(8)])


def get_key(data):
    print(hash(data))
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    print(hash_address)
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    print(hash_address)
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))