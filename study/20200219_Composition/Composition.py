## 포함(composition) 예제

class Person:
    def __init__(self):
        print('캐릭터 생성')

    def atteck(self):
        print('맨손 공격')

    def eat(self):
        print('물약 섭취')

class SwordMan(Person):
    def __init__(self):
        Person.__init__(self)
        print('검사 역할 부여')

    def atteck(self):
        print('장검 썰기')

    def skill1(self):
        print('파괴검일섬')

class Wizard(Person):
    def __init__(self):
        Person.__init__(self)
        print('마법사 역할 부여')

    def skill2(self):
        print('라이트닝 볼트')

'''
SwordMan과 Wizard를 상속해서 MagicWarrior 만드는 예제와 달리
SwordMan만 상속후 Wizard에서는 부분만 포함하는 개념을 사용함
결과는 같음
'''

class MagicWarrior(SwordMan):
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