'''
Design Pattern
객체 지향 프로그래밍 설계 경험을 통해 추천되는 설계 패턴을 기술한 것
실제 여러 프로그램을 설계해보면서 문제를 발견하고, 디자인 패턴을 적용해보아야 이해할 수 있음

Singleton pattern
클래스에 대한 객체가 단 하나만 생성되게 하는 방법

Observer pattern
객체의 상태 변경시, 관련된 다른 객체들에게 상태 변경을 통보하는 디자인 패턴
패턴 흐름
1) Observer 객체 생성
2) 객체상태가 변경시 통보하는 객체들 생성
3) Observer 객체에 통보하는 객체들 리스트에 등록
4) 객체 상태가 변경시 notify 메소드를 콜하면 등록되어 잇는 통보객체들이 notify 메소드에 구현된 기능 동작함


Builder pattern
생성자에 들어갈 매개 변수가 복잡하여 가독성이 떨어지고, 어떤 변수가 어떤 값인지 알기 어려움
전체 변수 중 일부 값만 설정하는 경우
20200217_OOP_Extend/CharacterAdvancementSystem.py 에 적용함

Factory pattern
Factory 클래스를 통해서만 객체를 생성한다


'''


## 싱글톤 객체 예시
class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class PrintObject(metaclass=Singleton):
    def __init__(self):
        print("This is called by super().__call__")

## 싱글톤 객체와 비교를 위해서 만든 일반 객체

class Test():
    def __init__(self, name, age):
        print("객체가 생성됨")
        self.name = name
        self.age = age

    def toString(self):
        print(self.name,"  ,", self.age)

object1 = PrintObject()
object2 = PrintObject()
print(object1)
print(object2)

test = Test('박종훈', 33)
test2 = Test('박종훈', 33)
test.toString()
test2.toString()

print(test)
print(test2)

## Observer pattern 예시
class Observer:
    def __init__(self):
        self.__observers = list()

    def notify(self, event_data):
        for observer in self.__observers:
            observer.notify(event_data)

    def register(self, observer):
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

class SMSNotifier:
    def notify(self, event_data):
        print(event_data, 'received...')
        print('send sms')

class EmailNotifier:
    def notify(self, event_data):
        print(event_data, 'received...')
        print('send email')

class PushNotifier:
    def notify(self, event_data):
        print(event_data, 'received...')
        print('send push notification')

print('')
print('------------Observer Pattern Start-----------------')
observer = Observer()

smsNotifier = SMSNotifier()
emailNotifier = EmailNotifier()
pushNotifier = PushNotifier()

observer.register(smsNotifier)
observer.register(emailNotifier)
observer.register(pushNotifier)

observer.notify("user login")

## Factory pattern
print('')
print('------------Factory Pattern Start-----------------')
class AndroidSmartphone:
    def send(self, message):
        print("send a message via Android platform")
        print("message: ", message)


class WindowsSmartphone:
    def send(self, message):
        print("send a message via Window Mobile platform")


class iOSSmartphone:
    def send(self, message):
        print("send a message via iOS platform")


class SmartphoneFactory(object):
    def __init__(self):
        pass

    def create_smartphone(self, devicetype):
        if devicetype == 'android':
            smartphone = AndroidSmartphone()  # <-- 실제 객체를 팩토리 클래스 안에서 만든다.
        elif devicetype == 'window':
            smartphone = WindowsSmartphone()  # <-- 실제 객체를 팩토리 클래스 안에서 만든다.
        elif devicetype == 'ios':
            smartphone = iOSSmartphone()  # <-- 실제 객체를 팩토리 클래스 안에서 만든다.
        return smartphone



smartphoneFactory = SmartphoneFactory()
android = smartphoneFactory.create_smartphone('android')
android.send('send email')