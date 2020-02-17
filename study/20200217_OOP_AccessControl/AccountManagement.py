## 계좌 관리 class 작성하기
## - attribute: 계좌 초기 금액을 속성으로 하나 설정
## - 생성자에서 초기 금액은 0으로 설정
## - 속성은 private 으로 설정
## - method: 인출, 저축, 잔액 확인 세 가지 method 구현, 각각 현재 계좌 금액 리턴

class AccountMangement:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance:
            print ('잔고의 금액이 부족합니다. 잔고금: ', self.__balance, '원')
        else:
            self.__balance = self.__balance - amount
            print (amount, '원이 인출되었습니다. 잔고액: ', self.__balance, '원')

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print('입금된 금액: ', amount, '원, 잔고금: ', self.__balance, '원')

    def balance(self):
        print('잔고금: ', self.__balance, '원')



bankCustomer = AccountMangement()
bankCustomer.deposit(2000)
bankCustomer.withdraw(1000)
bankCustomer.balance()