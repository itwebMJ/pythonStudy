'''
class Student:
멤버변수, name, num, kor, eng, math, total, avg //따로 변수로, 리스트, 클래스 포함관계
기능: 총점계산/ 평균계산/ 정보출력

리스트에 담지 말고 아래와 같이 객체 생성하여 실행
s1
s2
s3
'''
'''

class Score:
    def __init__(self, kor =0, eng=0, math=0):
        self.kor = kor
        self.eng = eng
        self.math = math

class Student:
    def __init__(self, name, num, kor, eng, math, total=0, avg=0):
        self.score = Score()
        self.name = name
        self.num = num
        self.score.kor = kor
        self.score.eng = eng
        self.score.math = math

        self.total = total
        self.avg = avg


    def s1(self):
        self.total = self.kor + self.eng + self.math
    def s2(self):
        self.avg = self.total/3
    def s3(self):
        # print('이름\t번호\t국어\t영어\t수학\t총점\t평균')
        print('name : ',self.name)
        print('num : ',self.num)
        print('kor : ',self.kor)
        print('eng : ',self.eng)
        print('math : ',self.math)
        print('total : ',self.total)
        print('avg : ',self.avg)

def main():
    std = Student('bbb','1',99, 88, 78)
    #std.s1('aaa','0',90, 80, 70)


    std.name = 'aaa'
    std.num = '0'
    std.kor = 90
    std.eng = 80
    std.math = 70

    std.s1()
    std.s2()

    std.s3()
main()
'''

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