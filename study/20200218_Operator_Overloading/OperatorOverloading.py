## 연산자 중복

class OperatorOverloading:
    def __init__(self, width, height, name):
        self.__width = width
        self.__height = height
        self.__name = name

    def __add__(self, second):
        return OperatorOverloading(self.__width + second, self.__height + second, self.__name)

    def __mul__(self, second):
        return OperatorOverloading(self.__width * second, self.__height* second, self.__name)

    def __len__(self):
        return (self.__width*2) + (self.__height*2)

    def getitem(self, index):
        if index == 0:
            return self.__width
        elif index == 1:
            return self.__height
        elif index == 2:
            return self.__name

    def __abcd__(self):
        return self.__height*self.__width

    def toString(self):
        print('width:', self.__width , ", height:", self.__height, ', name:', self.__name)


oo = OperatorOverloading(100, 4, 'jonghoon')
oo = oo + 2
oo.toString()
oo = oo * 4
oo.toString()
print(len(oo))
print(oo.getitem(0))

'''
연산자 중복과 정렬을 같이 쓰는 예
'''



class OperatorOverloadingExtend:
    def __init__(self, word):
        self.__word = word

    def __len__(self):
        return len(self.__word)

    def __getitem__(self, index):
        return self.__word[index]

    def get_word(self):
        return self.__word

Hi = OperatorOverloadingExtend('Hi')
Hello = OperatorOverloadingExtend('Hello')
Bye = OperatorOverloadingExtend('Bye')

Keywords = [Hi, Hello, Bye]

Keywords = sorted(Keywords, key=lambda  x: len(x))

for keyword in Keywords:
    print(keyword.get_word())

Keywords = sorted(Keywords, key=lambda  x: x[1])

for keyword in Keywords:
    print(keyword.get_word())


'''
Keyword 클래스를 생성
- 클래스 인자로 영어 단어 한 개를 받습니다.
- attribute: 영어 단어
- method: 연산자 오버로딩 - len() : 영어 단어 길이 리턴
프로그래밍 1. Keyword 클래스로 10개의 임의 영어 단어를 가지고 각각 객체로 만들어서 하나의 리스트에 넣습니다.(위 예 참조)

2. 영어 단어 길이를 기준으로 리스트를 정렬하기
- \__len\__(self) 정의하기
- sorted 함수와 lambda 로 길이 순 정렬 기법

3. 영어 단어의 두 번째 알파벳을 기준으로 리스트를 정렬하기
- \__getitem\__(self, key) 정의하기
'''

class KeywordObject:

    def __init__(self, word):
        self.__word = word

    def __len__(self):
        return len(self.__word)

    def __getitem__(self, index):
        return self.__word[index]
    def toString(self):
        print(self.__word)

mission = KeywordObject('mission')
africa = KeywordObject('africa')
item = KeywordObject('item')
solution = KeywordObject('solution')
way = KeywordObject('way')
member = KeywordObject('member')
human = KeywordObject('human')
group = KeywordObject('group')
union = KeywordObject('union')
subject = KeywordObject('subject')

KeywordList = [mission, africa, item, solution,
               way, member, human, group,
               union, subject]
KeywordList = sorted(KeywordList, key=lambda x:len(x))
print('')
for eachKeyowrd in KeywordList:
    eachKeyowrd.toString()

KeywordList = sorted(KeywordList, key=lambda  x:(len(x), x[1]))
print('')
for eachKeyowrd in KeywordList:
    eachKeyowrd.toString()

