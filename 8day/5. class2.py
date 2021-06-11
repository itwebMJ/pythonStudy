'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:(',self.x,' , ', self.y,')')

class Test:
    def __init__(self):
        self.num = 0       #정수
        self.s = ''         #문자열
        self.arr = []       #리스트
        self.point = Point()   #객체. 포함관계:클래스타입의 멤버변수 / 관계(포함관계-has a, 상속관계-is a)

    def printData(self):
        print('num:', self.num)
        print('s:', self.s)
        print('arr:', self.arr)
        #self.point.x = 20
        #self.point.y = 30
        self.point.printPoint()


def main():
    t1 = Test()#객체 생성
    t1.num = 10
    t1.s = 'hello class'
    t1.arr.append(1)
    t1.arr.append(2)
    t1.arr.append(3)
    t1.point.x = 20
    t1.point.y = 30
    #t1.point = Point(3,4)
    t1.printData()

main()
'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:(',self.x,' , ', self.y,')')

class Test:
    def __init__(self):
        self.p = Point()   #None 상수
        self.num = 0    #int 값

def main():
    t1 = Test() #Test 객체 생성 => 메모리 할당. 생성자를 호출해야 객체 메모리를 할당받는다
    t1.num = 10
    t1.p.x = 10
    t1.p.y = 20
    t1.p.printPoint()

main()