def f1():
    while True:
        menu = input('종료하려면 0 입력')
        print('입력값 : ',menu)
        if menu=='0':
            return #함수종료. None 상수 반환. 아무 값도 없다는 의미의 상수
def f2(name):
    return '당신의 이름은 ' + name #문자열 반환

def main():
    res = f1()
    print('f1의 리턴값 :', res)
    res = f2('aaa')
    print('f2의 리턴값 : ', res)

main()


