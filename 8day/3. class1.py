'''
객체 지향 프로그래밍
순차적 프로그래밍은 시간의 흐름 순서대로 코드를 짰다면 객체 지향 프로그래밍은 객체를 중심으로 개발.
객체를 정의하고 객체와 객체 사이의 관계를 정의하는 방식으로 프로그래밍 한다.

객체 : 세상을 프로그램으로 모델링 할 때 모델링의 대상이 되는 사람이나 사물, 개념. 즉 샘플.
객체를 샘플링

ATM
입금
출금 : 카드를 넣는다 => 카드 비밀번호 입력 => Yes => 출금액 입력 => 카드와 연결된 계좌 정보를 추출
                                        No =>

class 클래스명:

    def __init__(self): #생성자. 객체 초기화. 객체의 멤버변수 정의. 멤버변수란 클래스 소속의 변수.
        멤버변수 정의
    def 기능(self):
        실행문

'''
class Card:          #Card라는 이름의 타입을 정의함. 이 타입의 변수는 카드 1개의 정보를 담을 수 있다.
    '''

    def __init__(self):     #첫번째 파라미터는 현재 객체의 참조값을 받는다. 멤버변수 표현은 앞에 self, 변수이름
        self.number = ''    #카드번호
        self.owner  = ''    #카드명의자
        self.pwd  = ''      #카드비밀번호
        self.comp  =''      #카드사
    '''
    def __init__(self, number, owner, pwd, comp):
        self.number = number
        self.owner = owner
        self.pwd = pwd
        self.comp = comp

    #메서드. 멤버 함수
    def printCard(self):
        print(self.number)
        print(self.owner)
        print(self.pwd)
        print(self.comp)

def main():
    '''
    c1 = Card()
    c1.number = '123-4567-8913'
    c1.owner = '홍길동'
    c1.pwd = '111'
    c1.comp = '신한'
    c1.printCard()
    '''
    c1 = Card('123-4567-4567', '홍길동', '111', '신한')
    c1.printCard()
    c2 = Card('444-2312-1234', '홍길동2', '222', '현대')
    c2.printCard()
main()
