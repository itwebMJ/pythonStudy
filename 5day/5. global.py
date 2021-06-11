'''
id= 'aaa'
pw = '111'
input_id = input('id: ')
input_pw = input('pw : ')
if input_id == 'aaa' and input_pw =='111':
    print('로그인 성공')
else :
    print('잘못 입력')
'''
# 지역변수(지역구): 함수 내에서 선언. 그 함수 내에서만 사용가능
# 전역변수(전국구): 함수 밖에 선언. 이 파일 내에서 모든 함수에서 사용가능

num=10 #전역변수

def f1():
    global num  #전역변수로 지정
    num=20#전역변수. 전역변수 값 변경
    print('f1:', num)

def f2():
    x = 5#지역변수
    num = 15 #변수 정의. 지역변수로 정의
    print('f2 x:', x)
    print('f2 num:', num)#지역변수

def main():
    print('main num:', num)#전역변수
    #print('main x:', x) #다른 함수의 지역변수 사용불가
    f1()
    f2()
    print('main num:', num)#전역변수

main()