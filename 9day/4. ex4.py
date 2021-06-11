class Score: #1명의 점수 정보만 다루는 타입.
    def __init__(self, kor, eng, math):#멤버 변수는 점수와 관련된 국영수총평
        self.kor = kor
        self.eng = eng
        self.math = math
        #총점 평균 계산
        self.total = self.kor + self.eng + self.math
        self.avg = self.total/3

    def printScore(self):#점수와 관련된 국영수총평 출력
        print(self.kor, end='\t')
        print(self.eng, end='\t')
        print(self.math, end='\t')
        print(self.total, end='\t')
        print(self.avg, end='\t')
        print()

class Student:#1학생의 정보(score포함) 갖는 클래스
    def __init__(self, name, num, score):
        self.name = name
        self.num = num
        self.score = score  #Score객체. 포함관계

    def printMember(self):
        print(self.name, end='\t')
        print(self.num, end='\t')
        self.score.printScore()

def main():
    sc1 = Score(76,54,87)
    s1 = Student('aaa', 1, sc1)
    s1.printMember()

    s2 = Student('bbb', 2, Score(57,98,86))
    s2.printMember()

main()