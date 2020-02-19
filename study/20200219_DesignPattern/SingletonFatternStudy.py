import turtle as turtle

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
'''
shape 파라미터 - 도형 모양 의미 (string)
삼각형 그리기 - "triangle"
사각형 그리기 - "quadrangle"
오각형 그리기 - "pentagon"
육각형 그리기 - "hexagon"
원 그리기 - "circle"

'''
class Figure(metaclass=Singleton):
    def __init__(self):
        self.__pen = turtle.Pen()

    def draw_shape(self, shape, color, x, y):
        pen = self.__pen

        pen.pensize(4)

        pen.penup()
        pen.setx(x)
        pen.sety(y)
        pen.pendown()
        pen.begin_fill()
        pen.color(color)
        if shape == 'triangle':
            print('삼각형 만들기')
            pen.circle(40, steps=3)
        elif shape == 'quadrangle':
            print('사각형 만들기')
            pen.circle(40, steps=4)
        elif shape == 'pentagon':
            print('오각형 만들기')
            pen.circle(40, steps=5)
        elif shape == 'hexagon':
            print('육각형 만들기')
            pen.circle(40, steps=6)
        elif shape == 'circle':
            print('원 만들기')
            pen.circle(40)
        else:
            print('지원 하지 않는 도형입니다')
        pen.end_fill()

    def clear_shape(self):
        pen = self.__pen
        pen.clear()


figure = Figure()
figure.draw_shape('triangle', 'red', -200, -50)
figure.draw_shape('quadrangle', 'blue', -100, -50)
figure.draw_shape('pentagon', 'green', 0, -50)
figure.draw_shape('hexagon', 'yellow', 100, -50)
figure.draw_shape('circle', 'green', 200, -50)