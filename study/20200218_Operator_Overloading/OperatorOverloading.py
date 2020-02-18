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


