'''
클래스
int, float, str.. 이러한 기본 타입으로 객체 표현 어려움 => 객체 표현할 수 있는 데이터타입 정의.

학생의 이름, 번호, 학과
데이터 여러개 담으라고 리스트 제공

['aaa', 1, '컴공', 'bbb', 2, '산디', 'ccc', 3, '전자']

[['aaa', 1, '컴공'], ['bbb', 2, '산디'], ['ccc', 3, '전자']] => 2차원 리스트.


=> 리스트는 차수가 올라갈수록 복잡도가 올라간다

=> 학생의 문제점: 한 객체가 갖는 데이터 값도 여러개, 타입도 여러종류 => 하나의 기본 타입 변수에 담지 못함.
=> 리스트 사용시 복잡도 올라감
=> 에잇 타입을 만들자 => 클래스

<클래스 사용법>
1. 타입을 만든다 => 클래스 정의
2. 타입으로 변수를 만든다 => 객체 생성 => 메모리 할당받음
3. 만든 변수에 값 할당 => 객체 멤버 변수에 값 할당
   값을 읽을 수 있음
4. 메서드도 호출 가능

멤버변수는 다른 메서드에서도 만들 수 있지만 호출 순서에 따라 에러가 발생할 수 있으므로 멤버변수는 생성자에서 정의하는 것이 좋다
class Test:
    def setData(self, a, b):  #이 메서드에서 멤버변수 정의.
        self.a = a
        self.b = b

    def printData(self):
        print('a:', self.a)
        print('b:', self.b)


def main():
    m1 = Test()
    m1.setData(1,2)
    m1.printData()

    m2 = Test()
    m2.printData()
    m2.setData()

main()
'''
#클래스 구성요소: 멤버변수(이 객체의 데이터 담을라구), 메서드(기능)
#vo 클래스 => 역할: 객체의 값 저장. 값 관련 (메서드)기능만 제공. 값 할당(생성자), 값변경, 값읽기
#모니터 재고 관리 프로그램. 모델명, 가격, 수량, 크기
#모니터를 코드로 변환 => 하나의 모니터를 표현할 수 있는 타입 정의 => 모니터 클래스를 정의

#클래스 정의. 파이썬의 모든 클래스는 자동으로 object클래스를 상속받는다. 그래서 object가 가지고 있는 모든 멤버변수와 메서드를
#자동으로 상속받음
#그 중 하나가 __str__(): 객체를 설명하는 문자열을 반환. 클래스명 and 할당받은메모리 참조값을 문자열로 반환
class Monitor:
    #생성자. 객체 초기화하는 함수. 멤버변수 정의 및 초기화. self:현재 객체 참조값. 모든 메서드는 첫번째 파라메터가 self다
    #멤버변수:객체소속의 변수. self.변수
    def __init__(self, model='', price=0, amount=0, size=0):
        self.model = model
        self.price = price
        self.amount = amount
        self.size = size

    def printMonitor(self):
        print('model:', self.model)
        print('price:', self.price)
        print('amount:', self.amount)
        print('size:', self.size)



def main():
    m1 = Monitor('s2440', 1500, 5, 27)  #객체 생성
    m1.printMonitor()

    m2 = Monitor('s2455', 2500, 5, 30)
    m2.printMonitor()

    m3 = Monitor('s3440', 4500, 8, 30)
    m3.printMonitor()

main()