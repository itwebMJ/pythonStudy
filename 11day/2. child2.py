class Parent:
    def __init__(self):
        self.a = 10
        print('Parent 생성자')

    def method1(self):
        print("메서드1")

class Child(Parent):		#Child는 Parent를 상속받는다. 부모의 멤버변수와 메서드를 물려받는다
    def __init__(self):	    #super() : 부모객체 반환
        super().__init__()   #부모객체 생성
        print('Child생성자')
        self.b = 20
    def method2(self):
        print("메서드2")

def main():
    c1 = Child()
    print('c1.a : ', c1.a)
    print('c1.b : ', c1.b)
    c1.method1()
    c1.method2()

main()