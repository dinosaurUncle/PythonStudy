'''
캐릭터 전직 시스템

level 1~20 까지 평민
level 20~40까지 검사, 궁수, 마법사 중 선택이 가능하다
level 40~60까지 기사, 사냥꾼, 흑마법사 전직이 가능하다

만들어야 하는 메서드는 레벨업, 공격, 전직 가능여부, 캐릭터정
각 클래스 별 콘솔 메세지
평민: 맨 손 공격
-- 1차 전직 --
검사: 1단 베기
궁수: 화살 쏘기
마법사: 불꽃 던지기
-- 2차 전직 --
기사: 10단 연속 베기
사냥꾼: 연속 12화살 쏘기
흑마법사: 메테오

속성: 레벨, 제한레벨, 직업, 전직수, 공격방식 이다

전직 가능여부는 True, False의 값으로 반환되며
전직 가능여부가 되어야 전직 할 수 있다
단 전직 이후에 다른 전직으로 교환불가

게임 종료방법
2차 전직 이후 레벨 100이 넘으면 종료된다
'''

class CommonCharcter:
    def __init__(self):
        self._level = 1
        self._job = '무직'
        self._adbanceNum = 0
        self._attack = '맨손 공격'
        self._limmitLevel = 20

    def attack(self):
        print(self._attack)

    def levelUp(self):
        if (self._level >= self._limmitLevel):
            print('전직해야 레벨이 올라갑니다~!')
        else :
            self._level = self._level+1
            print('레벨이 상승하였습니다! 현재 레벨: ', self._level)

    def getLevelNum(self):
        return self._level
    def adbance(self):
        if (self._level == self._limmitLevel):
            return True
        else :
            print('전직하기에는 레벨이 부족합니다')
            return False

    def getAdbanceNum(self):
        return self._adbanceNum
    def getJob(self):
        return self._job보

    def showCharcter(self):
        print('레벨: ', self._level)
        print('직업: ', self._job)
        print('전직수:', self._adbanceNum)

class OneJobChange(CommonCharcter):
    def __init__(self):
        self._level =20
        self._adbanceNum = 1
        self._limmitLevel = 40

        while True:
            print("계열을 선택하시오: 검, 활, 마법")
            isBrack = False
            selectCommand = input()
            if selectCommand == '검':
                self._job = '검사'
                self._attack = '1단 베기'
                isBrack = True
            elif selectCommand == '활':
                self._job = '궁수'
                self._attack = '화살 쏘기'
                isBrack = True
            elif selectCommand == '마법':
                self._job = '마법사'
                self._attack = '파이어볼'
                isBrack = True
            if isBrack:
                print(self._job, '로 1차 전직')
                break
            else :
                print('잘못된 입력입니다')

class TwoJobChange(OneJobChange):
    def __init__(self, job):
        self._level =40
        self._adbanceNum = 2
        self._limmitLevel = 60
        if job == '검사':
            self._job = '기사'
            self._attack = '10단 연속 베기'
        elif job == '궁수':
            self._job = '사냥꾼'
            self._attack = '연속 12화살 쏘기'
        elif job == '마법사':
            self._job = '흑마법사'
            self._attack = '메테오'

        print(self._job, '로 2차 전직')


common = CommonCharcter()
while common.getLevelNum() < 60:
    command = input()
    if command == 'attack':
        common.attack()
    elif command == 'levelup':
        common.levelUp()
    elif command == 'adbance':
        if common.adbance():
            if common.getAdbanceNum() == 0:
                common = OneJobChange()
            elif common.getAdbanceNum() == 1:
                common = TwoJobChange(common.getJob())
            elif common.getAdbanceNum() == 2:
                break
    elif command == 'showCharcter':
        common.showCharcter()

print('게임 클리어')