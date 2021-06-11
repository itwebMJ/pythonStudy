a=10 #전역변수
def f1(param1):#param1:지역변수
    b = 20 #지역변수
    print('a:', a)#전역변수 a
    print('param1:', param1)
    print('b:', b)

def f2():
    a=30  #새 지역변수 정의
    print('a:', a)
    #print(b)       #f1의 지역변수이므로 사용불가
    #print(param1)  #f1의 지역변수이므로 사용불가

def f3():
    global a
    a=50#전역변수 a변경
    print('a:', a)#전역변수 출력
    #print('x:', x)  #x는 전역변수 이지만 호출 이후에 선언해서 안보임

def main():
    f1(35)
    f2()
    f3()

main()

x = 100  #전역변수