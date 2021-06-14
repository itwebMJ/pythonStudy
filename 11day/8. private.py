'''
접근 제어 : 클래스의 멤버변수나 메서드를 외부에서의 접근을 허용 여부 지정
private : 이름앞에 __를 붙임. 클래스 밖에서 안보임. 직접사용안됨. 데이터 은닉성 제공. public 메서드로 우회적으로 접근 가능
pub;ic : 일반 멤버 변수와 메서드. 클래스 밖에서 보임. 클래스 밖에서도 사용 가능.
'''

class Test:
    def __init__(self):
        self.__a = 10   #private 멤버
        self.b = 20     #public 멤버

    def setData(self, a, b):
        self.__a = a
        self.b = b

    def printData(self):
        print('a:', self.__a)
        print('b:', self.b)

    def setA(self, a):  # setter : 클래스 밖에서 private 멤버에 값을 설정하는 메서드
        self.__a = a

    def getA(self):  #getter : 클래스 밖으로 private 멤버 값을 반환하여 외부에서도 읽을 수 있게 하는 메서드
        return self.__a

def main():
    t1 = Test()
    t1.printData()
    t1.setData(3, 4)
    t1.printData()

    t1.setA(100)
    t1.b = 200

    print('t1.a : ', t1.getA())
    print('t1.b : ', t1.b)

main()