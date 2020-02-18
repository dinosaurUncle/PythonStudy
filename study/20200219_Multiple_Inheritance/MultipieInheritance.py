## 다중 상속 예제

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

class MagicianWarrior(SwordMan, Wizard):
    def __init__(self):
        SwordMan.__init__(self)
        Wizard.__init__(self)
        print('직업 혼합 효과 매직 워리어 역할 부여')

    def mixSkill(self):
        print('번개 자르기 일섬')


character = MagicianWarrior()
character.atteck()
character.eat()
character.skill1()
character.skill2()
character.mixSkill()