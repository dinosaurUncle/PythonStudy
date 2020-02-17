## 피자 가게 관리 class 작성하기
## - attribute: 피자 종류(리스트 데이터 타입), 피자 가게 이름 속성
## - 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정, 피자 종류는 ['슈퍼슈프림', '콤비네이션', '불고기']로 제공
## - 각 속성은 private 으로 설정
## - method: 원하는 피자를 제공하는지를 알려주는 기능, YES 또는 NO 문자열을 리턴

class PizzeriaManagement:
    def __init__(self, pizzaType, pizzaStoreName):
        self.__pizzaType = pizzaType
        self.__pizzaStoreName = pizzaStoreName

    def orderAvailability(self, pizzaName):
        result = False
        for pizza in self.__pizzaType:
            if pizza == pizzaName:
                result = True
        if result :
            return 'YES'
        else :
            return 'NO'

    def orderVersion(self):
        print(self.__pizzaStoreName, '메뉴판')
        print('가능메뉴: ', self.__pizzaType)



pm = PizzeriaManagement(['슈퍼슈프림', '콤비네이션', '불고기'], '종훈피자')
pm.orderVersion()
print('슈퍼슈프림 피자 주문 가능한가요? ', pm.orderAvailability('슈퍼슈프림'))