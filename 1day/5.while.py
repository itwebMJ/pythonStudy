'''
a = 5
while a>0:
    print(a)
    a-=1
print('while 밖')


#1-10까지 출력
a = 1
while a<=10:
    print(a)
    a+=1
'''
'''
1, 1-100 합 5050
2. 2-100 짝수출력
3.구구단 단수를 입력받아 한 단 출력
4. 약수구하기 (약수구할 숫자 입력받아) 6 : 1, 2, 3
'''
'''
a = 1
num = 0
while a<=100:
    #print(a)
    num += a
    a+=1
print('1부터 100까지 합 = ', num)

b = 1
while b<=100:
    b+=1
    if b%2 ==0:
        print(b)

c= int(input('구구단의 단 입력 : '))
a=0
while a<9:
    a+=1
    print(c, ' * ',a,' = ', c * a)

d= int(input('약수를 구할 수 입력 : '))
e=1
while d >= e:
    if d % e == 0 :
        print(int(d / e) )
    e += 1
'''
'''
i=1 #루프에서 사용할 변수를 정의. 카운팅 함수
while i<=100:
    print(i, end='\t')
    if (i%10) ==0 :
        print()
    i+=1
i=1 #루프에서 사용할 변수를 정의. 카운팅 함수
while i<=100:
    if (i%2) ==0 : #짝수
        print(i, end='\t')
    i+=1
print()
i=2
while i<=100:
    print(i, end='\t')
    i+=2
print()
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print('sum :', sum)
print()
'''
# 1-100 사이의 소수(약수가 1과 자신밖에 없는 수)를 출력

print('다운카운팅으로 # 3개출력')
i=3
while i>0:
    print('#', end='')
    i-=1
print()

print('업 카운팅으로 # 3개출력')
i=1
while i<=3:
    print('#', end='')
    i+=1
print()


print('업 카운팅으로 # 3개출력')
j=1
while j<3:
    i=1
    while i<=3:
        print('#', end='')
        i+=1
    print()
    j+=1
#조건에 의한 반복
score =200
while score >100 or score < 0:
    score = int(input('score(0-100) : '))
if score >60 :
    print('합격')
else :
    print('불합격')
