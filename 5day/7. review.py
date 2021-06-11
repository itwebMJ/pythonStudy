# 1. 변수: 한 개의 값 저장.
# 변수를 정의해서 사용. 정의시 할당한 값의 타입이 그 변수의 타입으로 결정
a = 10  # int
b = '11'  # str
c = True  # bool
d = 23.345  # float

e = a + int(b)
f = str(a) + b

print(e)
print(f)

a = 10
print(a > 10)
print(a == 10)

b = (a == 10)
if b:
    print('a는 10과 같다')
else:
    print('a는 10과 같지않다')

######################################
'''
연산자
1. 산술연산자
+, -, *, **, /, //, %

2. 비교연산자
>, >=, <, <=, ==(같다), !=(같지 않다)
'''

a, b, c = 10, 15, 10

print('a>b:', a > b)
print('a>=b:', a >= b)
print('a<b:', a < b)
print('a<=b:', a <= b)
print('a==b:', a == b)
print('a!=b:', a != b)
print('a==c:', a == c)
print('a!=c:', a != c)

# 3. 논리 연산자(bool값에 대한 연산): ex> True and Flase / True or Flase / not True
# and: 피 연산자 모두 True일때만 True, 나머지 False
a, b, c = 10, 15, 10
print(a == 10 and b < 10)  # False

# or: 피 연산자 하나만 True이면 True
print(a == 10 or b < 10)  # True

# not: 반전
print(not a == 10)  # False

# 4. 대입연산자: = (오른쪽의 값을 왼쪽에 할당)
a = 10  # 오른쪽의 10을 왼쪽 변수 a에 대입
a += 2  # a = a+2
a -= 2  # a = a-2
a *= 2  # a = a*2
a /= 2  # a = a/2
# ...

########################################
'''
제어문: 프로그램 문장의 흐름을 제어하는 문
1. 조건문: ATM 출금. 카드를 넣는다. 카드 비밀번호를 입력한다 ->YES -> 출금할 금액을 입력
                                                      ->NO -> 비밀번호 다시 입력

위의 예처럼 한 상황에서 여러 경우의 수가 발생했을때 이를 조건문으로 구현
조건을 따져서 True, False에 따라 실행문 다르게 구현

1) if문: 조건을 만족할 경우 실행할 코드만 구현. 조건을 만족하면 if블록 실행하고 조건이 False이면 건너뜀
if 조건:
    실행문


a=11
if a==10:
    print('a는 10이다. ')

#2) if 조건 - else문: 조건 하나를 명시하고 이 조건이 True이면 if블록을 실행하고 False이면 else블록을 실행. 합격/불합격, 짝수/홀수
score = 67
if score>=60:
    print('합격')
else:
    print('불합격')

id='aaa'
pwd='111'
id2 = input('id')
pwd2 = input('pwd')
if id==id2 and pwd==pwd2:
    print('로그인 성공')
else:
    print('로그인 실패')

#3) if 조건1 - elif 조건2 - elif 조건3 - else문:
# 다양한 조건을 제시하여 True인 조건블록만 실행하고 종료.
# 어느 조건도 True가 아니면 else블록 실행

menu = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.종료')

if menu=='1':
    print('밥먹는다')
elif menu=='2':
    print('잠잔다')
elif menu=='3':
    print('운동한다')
elif menu=='4':
    print('논다')
elif menu=='5':
    print('종료')
else:
    print('잘못된 메뉴')

print('if밖')
'''

'''
2. 반복문: 특정문장을 조건을 만족하는 동안이나(while문), 지정한 횟수만큼 반복하는(for문) 문

1)while문: 조건을 따져서 True이면 반복하고 False이면 빠져나감

while 조건:
   실행문


while True:
    print('무한루프')
    num = int(input('멈추려면 0을 입력하라'))
    if num == 0:
        break#루프를 나가라

print('while 밖')


a=5
while a>0:#조건이 True일 동안 반복
    print(a)
    a-=1

print('while 밖')

#2)for문: 리스트, 문자열 등 나열된 값의 개수 만큼 반복하고자 할때. 지정한 횟수 만큼 반복하고자 할때 사용
a=[1,2,3,4,5,6,7]
for i in a:#in 다음에 나오는 값들 개수 만큼 반복. 값들을 순서대로 삥글 한번에 하나씩 뽑아서 i에 할당
    print(i)

print('for 밖')

b = 'abcdefghijk'
for i in b:
    print(i)
print()

for i in range(-1, -12, -1):
    print(b[i])
print()

for i in range(1, len(b)+1): #b[0:5] => abcde
    print(b[0:i])
print()


#range(시작값, 끝값, 간격). 간격 생략하면 기본 1
for i in range(0, 5):#0,1,2,3,4
    print(i)
print()

for i in range(1, 5):#1,2,3,4
    print(i)
print()

for i in range(1, 30, 3):
    print(i)
print()

#별표 100개를 찍는데 10개씩 줄바꿈
for i in range(0, 100):
    print('*', end='')
    if i%10==9:
        print()
print()
'''
'''
1)삼각형
*
**
***
****
'''
line = int(input('크기:'))
for i in range(1, line + 1):  # 줄수
    for j in range(0, i):  # 한 줄에 출력될 별 개수
        print('*', end='')
    print()

'''    
2)삼각형
    *
   **
  ***
 ****
*****
'''
line = int(input('크기:'))  # 줄수
cnt = 4
for i in range(1, line + 1):  # 줄만들기. 4,3,2,1,0
    ch = ' '  # 출력할 문자
    for j in range(0, line):  # 한줄에 문자 출력
        if j == cnt:
            ch = '*'
        print(ch, end='')
    cnt -= 1
    print()