#Person 사람. 이름, 나이 저장. 기능 출력.
#객체 2개 생성
#클래스: 멤버변수(속성), 메서드

class Person: #클래스 정의
    def __init__(self, name='', age=0):#생성자는 아무때나 호출 못하고 생성할 때 한번만 호출됨
        #멤버 변수 정의. 객체의 데이터를 담는 변수.
        self.name = name
        self.age = age

    def setData(self, name, age):
        self.name = name
        self.age = age

    #메서드. 클래스 안에 정의한 함수. 이 객체의 기능. 정보 출력
    #모든 메서드의 첫번째 파라메터는 현재 객체의 참조값이 자동으로 전달됨.
    def printPerson(self):  #현재 객체의 참조값
        name='xxx'
        print('지역변수 name:', name)
        print('name:', self.name)
        print('age:', self.age)

def main():
    p1 = Person('aaa', 12)#생성자 호출은 클래스명() => 객체가 사용할 메모리 할당받아서 그 참조값을 반환
    p1.printPerson()

    p2 = Person()  # 생성자 호출은 클래스명() => 객체가 사용할 메모리 할당받아서 그 참조값을 반환
    p2.printPerson()

main()