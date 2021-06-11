a=10
b=13
'''
#조건문은 조건이 만족될 때 실행됨
if a>b:
     print('a는 b보다 크다')
if a==b:
     print('a는 b와 같다')
if a < b:
     print('a는 b보다 작다')
'''
'''

#합격 불합격 체크 . 점수를 입력받아 60점 이상이면 합격 출력
score = int(input('점수를 입력하시오 :'))
if score >= 60 :
    print('합격')
else :      #if조건이 만족되지 않으면 실행되는 불록. score < 60
    print('불합격')

'''
'''
#숫자를 입력받아 짝수면 짝수, 홀수면 홀수 입력
num = int(input('숫자를 입력하시오 :'))
if num%2 == 0:
    print('짝수')
else:
    print('홀수')
'''
'''
#성별과 나이를 입력받아 성인여성일 때만 통과, 그렇지 않으면 통과불가

age = int(input('나이를 입력하시오 :'))
if age >= 20:
    gender = input('성별(여 :f, 남: m) : ')

    if gender =='f':
        print('입장')
    else:
        print('여성만 입장가능')
else:
    print('성인만 입장가능')

age = int(input('나이를 입력하시오 :'))
gender = input('성별(여 :f, 남: m) : ')

if age >=20 and gender =='f':
    print('입장')
else:
    print('성인 여성만 입장가능')

if age >=20 or gender =='f':
    print('입장')
else:
    print('성인이거나 여성만 입장가능')
'''

score = int(input('점수를 입력하시오 (0-100):'))
if score < 0 or score > 100 :
    print('잘못 입력했습니다')
else:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
