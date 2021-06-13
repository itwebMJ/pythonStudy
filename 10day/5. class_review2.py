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

    #메서드 오버라이딩.=> 상속받은 메서드를 수정해서 사용
    def __str__(self):#객체 설명 메서드로 object로부터 상속받았음.
        return 'model:'+self.model+' / price:'+str(self.price)+' / amount:'+str(self.amount)+' / size:'+str(self.size)


def main():
    monitors = []#방이 없음
    monitors.append(Monitor('s2440', 1500, 5, 27))
    monitors.append(Monitor('s2455', 2500, 5, 30))
    monitors.append(Monitor('s3440', 4500, 8, 30))

    for i in range(0, 3):
        print(monitors[i])

    for m in monitors:
        print(m)

main()