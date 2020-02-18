from abc import *

'''
S - SRP(Single responsibility principle) 단일 책임 원칙
클래스는 단 한개의 책임을 가져야 함 (클래스를 수정할 이유가 오직 하나이어야 함)
계산기 기능 구현시, 계산을 하는 책임과 GUI를 나타낸다는 책임을 서로 분리하여, 각각 클래스로 설계해야 함
예제 코드는 생략
함
O - OCP(Open Closed Principle) 개방 - 폐쇄 원칙
확장에는 열려있어야 하고, 변경에는 닫혀있어야 함
-> 기본 캐릭터와 전직 캐릭터
캐릭터 마다 행동이 틀리다고 한다면 각각의 메소드를 따로 만드는 것이 아니라
상속을 받아서 메소드 오버라이딩으로 해결하는 방식
동일 행동은 기본 캐릭터에서 구현해서 상속 받음
(아래 예제 있음)

L - LSP(Liskov Substitusion Principle) 리스코프 치환 법칙
-> 자식 클래스는 언제나 자신의 부모클래스와 교체할 수 있다는 원칙
예제: 20200217_OOP_Extend/CharacterAdvancementSystem.py
전직 레벨이 되면 자식 클래스 교체함(코드참조)
-> 다형성

I - ISP(Interface Segregation Principle) 인터페이스 분리 원칙
부모클래스에서 사용하지 않는 메소드는 선언만 하고 자식 클래스에서 구현함
-> 선언만 하는 클래스는 추상메소드라고함
-> 선언한 메소드는 상속받은 자식 클래스에서는 반드시 구현해야 함

D - DIP(Dependency Inversion Principle) 의존성 역전 법칙
-> 자식클래스 내부에서 부모 클래스 객체 생성을 하면 안되고 부모 객체를 클라이언트 단에서 생성하여
자식 클래스 내부로 부모 객체를 주입해야 한다

'''





## OCP(Open Closed Principle) 개방 - 폐쇄 원칙 예제
'''
                    Person
                      |
        |-------------|-----------|
        SwordMan    Archer     Wizard
        
        공격방식        
        1) Person: 주먹 날리기
        2) SwordMan: 검 휘둘르기
        3) Archer: 화살 발사
        4) Wizard: 파이어볼
        
        포션섭취: 동일 
        
                 
'''

class Person:
    def attack(self):
        print('주먹 날리기')
    def eat(self):
        print('힐링 포션 섭취')

class SwordMan(Person):
    def attack(self):
        print('검 휘둘르기')

class Archer(Person):
    def attack(self):
        print('화살 발사')

class Wizard(Person):
    def attack(self):
        print('파이어볼')

person = Person()
swordMan = SwordMan()
archer = Archer()
wizard = Wizard()

characters = [person, swordMan, archer, wizard]

for character in characters:
    character.attack()
    character.eat()

## I - ISP(Interface Segregation Principle) 인터페이스 분리 원칙 예제

class Car(metaclass=ABCMeta):
    @abstractmethod
    def rash(self):
        pass

class K3(Car):
    def rash(self):
        print('최고 출력 128마력')


class A6(Car):
    def rash(self):
        print('최고 출력 605마력')


car = K3()
car.rash()


## D - DIP(Dependency Inversion Principle) 의존성 역전 법칙

'''
잘못되 예제
-> MagicWarrior 안에서 객체를 생성

class Person2:
    def __init__(self):
        print('캐릭터 생성')

    def atteck(self):
        print('맨손 공격')

    def eat(self):
        print('물약 섭취')

class SwordMan2(Person2):
    def __init__(self):
        Person.__init__(self)
        print('검사 역할 부여')

    def atteck(self):
        print('장검 썰기')

    def skill1(self):
        print('파괴검일섬')

class Wizard2(Person2):
    def __init__(self):
        Person.__init__(self)
        print('마법사 역할 부여')

    def skill2(self):
        print('라이트닝 볼트')


class MagicWarrior(SwordMan2):
    def __init__(self):
        self.__Wizard = Wizard()

        print('직업 혼합 효과 매직 워리어 역할 부여')
    def skill2(self):
        return self.__Wizard.skill2()

    def mixSkill(self):
        print('번개 자르기 일섬')


character = MagicWarrior()
character.atteck()
character.eat()
character.skill1()
character.skill2()
character.mixSkill()

'''
class Person2:
    def __init__(self):
        print('캐릭터 생성')

    def atteck(self):
        print('맨손 공격')

    def eat(self):
        print('물약 섭취')

class SwordMan2(Person2):
    def __init__(self):
        Person.__init__(self)
        print('검사 역할 부여')

    def atteck(self):
        print('장검 썰기')

    def skill1(self):
        print('파괴검일섬')

class Wizard2(Person2):
    def __init__(self):
        Person.__init__(self)
        print('마법사 역할 부여')

    def skill2(self):
        print('라이트닝 볼트')

## MagicWarrior 클래스는 코정이며 주입받는 객체는 외부에서 언제든지 변경이 가능하게 만들어야 함
class MagicWarrior(SwordMan2):
    def __init__(self, wizard):
        self.setSill2Object(wizard)
        print('직업 혼합 효과 매직 워리어 역할 부여')

    def setSill2Object(self, wizard):
        self.__wizard = wizard

    def mixSkill(self):
        print('번개 자르기 일섬')

    def skill2(self):
        self.__wizard.skill2()

character = MagicWarrior(Wizard2())
character.atteck()
character.eat()
character.skill1()
character.skill2()
character.mixSkill()