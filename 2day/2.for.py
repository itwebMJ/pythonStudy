b=[1,2,3,4,5]
'''
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])

for i in [1,2,3,4,5]:
    print(i)

for i in b:
    print(i)

for i in 'hello world':
    print(i)

for i in range(0, 5): #[0,1,2,3,4]
    print(i)

for i in range(1, 10, 2): #[1,3,5,7,9] range(시작값, 끝값, 간격)
    print(i)
'''
'''
1~10 출력
1-10 사이의 짝수 출력
1-100까지의 합
구구단 3단
'''
'''
for i in range(1,11):
    print(i, end='\t')
print()

for i in range(2,11,2):
    print(i, end='\t')
print()

num = 0
for i in range(1,101):
    num += i
print(num)

for i in range(1,10):
#    num += i
    print('3 * ', i, ' = ',i*3)

for j in range(2, 10):
    for i in range(1, 10):
        print(j, ' * ', i, ' = ', i*j)
'''
'''
1. 1-100 소수 출력 
2. 크기 입력받아 삼각형 출력
*
**
***
****

3. 크기 입력받아 삼각형 출력
*
**
***
****
*****

4. 크기 입력받아 삼각형 출력
*
***
*****

5. 크기 입력받아 마름모 출력
*
***
*****
***
*
'''
'''
#1. 1-100 소수 출력
for i in range(1,101):
    e=0 # 약수의 개수
    for j in range(1, 101):
        if i % j == 0:
            e+=1
    if e == 2 :
        print('소수 : ',i)

#2. 크기 입력받아 삼각형 출력
input_data = int(input('출력할 삼각형의 크기를 입력 : ')) + 1
for i in range(1, input_data):
    print('*'*i)
    
#3. 크기 입력받아 삼각형 출력
input_data = int(input('출력할 삼각형의 크기를 입력 : '))
i = 1
for j in range(input_data, -1, -1):
    print(' '*j, end='*'*i)
    i+=1
    print()
'''
#4. 크기 입력받아 삼각형 출력
input_data = int(input('출력할 삼각형의 크기를 입력 : '))
k = 1
for j in range(input_data, -1, -1):
    print(' '*j, end='')
    print('*' * k)
    k+=2

#5. 크기 입력받아 마름모 출력
input_data = int(input('출력할 마름모의 크기를 입력 : '))
k = 1
for j in range(input_data, -1, -1):
    print(' '*j, end='')
    print('*' * k)
    k+=2
for j in range(1, input_data+1):
    k-=2
    print(' ' * j, end='')
    print('*'*(k-2))
