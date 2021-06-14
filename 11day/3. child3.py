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
        self.c = 30
        self.d = 40
    
    def method2(self):
        print("메서드2")
    def method3(self):
        print("메서드3")

def main():
    c1 = Child()
    print('c1.a : ', c1.a)
    print('c1.b : ', c1.b)
    c1.method1()
    c1.method2()

    c2 = Child()
    print('c2.c : ', c2.c)
    print('c2.d : ', c2.d)
    c2.method1()
    c2.method3()

main()