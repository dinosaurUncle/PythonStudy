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

