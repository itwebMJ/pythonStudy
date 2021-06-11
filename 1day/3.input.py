'''
키보드 입력
print() : 출력
input() : 키보드 입력
'''

'''
#input()로 받은 값을 name에 저장
name = input('이름을 입력하시오 : ')
print('name : ', name)

age = input('나이을 입력하시오 : ')
print('age : ', age)
print('10년 뒤 age : ', int(age)+10)
'''

'''
#캐스팅함수
int('123')      => 123
float('23.345') => 23.345
str(12)         =>'12'
'''

#숫자 2개를 입력받아 +, -, =, / 연산의 결과르 출력하시오.

first =int(input('첫번째 숫자를 입력하시오 : '))
second = int(input('두번째 숫자를 입력하시오 : '))

print(first,' + ',second, ' =', first + second)
print(first,' - ',second, ' =', first - second)
print(first,' * ',second, ' =', first * second)
print(first,' / ',second, ' =', first / second)
