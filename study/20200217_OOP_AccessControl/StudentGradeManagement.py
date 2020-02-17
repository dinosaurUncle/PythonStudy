##학생 성적 관리 class 작성하기
##- attribute: 국어, 영어, 수학, 학생 이름 네 개의 속성
##- 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
##- 각 속성은 private 으로 설정
##- method: 전체 과목 점수 평균, 전체 과목 총점 두 가지 method 구현

class StudentGradeMangement:
    def __init__(self, korean_score, english_score, math_score):
        self.__korean_score = korean_score
        self.__english_score = english_score
        self.__math_score = math_score

    def grade_average(self):
        if (self.__korean_score + self.__english_score + self.__math_score) != 0:
            return ((self.__korean_score + self.__english_score + self.__math_score)/3)
        else :
            return 0


student = StudentGradeMangement(90, 85, 100)
print ('성적 평균은: ', student.grade_average())
