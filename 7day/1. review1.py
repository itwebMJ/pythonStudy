'''

def printName(str):
    print('파라미터 : ', str)

def maxNum(num1, num2, num3):
    max=num1

    if max < num2:
        max  =num2
        if max<num3:
            max = num3
    elif max < num3:
        if num2 < num3:
            max = num3
        else:
            max = num2
    return max

def sumNum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum

def f1(str='aaa', num=0):
    print('str : ',str, ', num : ',num)

def main():
    printName(input('printName 입력 : '))
    print('max 값 :' ,maxNum(40, 30, 50))
    print('sum : ',sumNum([1, 2, 3, 4, 5]))
    f1()
    f1('bbb',1)
main()
'''

#1. 이름이 printName이고 파라메터로 문자열하나를 받아서 간단히 받은 파라메터값을 출력하는 함수를 정의하고 호출. 함수 리턴값 없음

#함수정의
def printName(x):
    print(x)

#함수호출
printName('asdf')

#2. 파라메터로 숫자 3개를 받아서 이중 가장 큰 값을 반환하는 함수. 이름은 maxNum 함수 정의 및 호출

def maxNum(n1, n2, n3):
    if n1>=n2:
        m = n1
    else:
        m = n2
    if m < n3:
        m = n3
    return m

max_num = maxNum(7,4,9)
print('max_num:', max_num)

#3. 파라메터로 리스트하나를 받아서 리스트에 담긴 숫자 모두의 합을 구하여 반환하는 함수를 정의 및 호출. 함수 이름은 sumNum
def sumNum(arr):
    s = 0
    for i in arr:
        s+=i
    return s

list_sum = sumNum([1,2,3,4,5])
print('list_sum:', list_sum)

#4. 파라메터로 문자열하나 숫자하나를 받는 이름이 f1인 함수 정의. 호출시 파라메터의 순서가 바뀌어도 동작되도록 정의 및 호출하시오.
#동작은 파라메터 값 출력하고 리턴값은 없음

def f1(s, n):#s:문자열, n:숫자
    print('s:', s)
    print('n:', n+4)

#f1(10, 'aads')
f1(n=10, s='asdf')#키워드 인자:각 아규먼트가 어느 파라메터변수로 저장될지 지정. 순서 바꿔도 잘됨

#5. 위 f1함수 파라메터의 기본값을 설정하시오. 문자열파라메터의 기본값은 'aaa', 숫자파라메터의 기본값은 0 이다
def f1(s='aaa', n=0):#s:문자열, n:숫자
    print('s:', s)
    print('n:', n+4)

f1('asd', 123)
f1()#기본값을 지정한 파라메터는 호출시 값 할당을 생략가능

#파라메터의 기본값이 지정된것과 지정되지 않은것을 섞어서 쓸때 순서가 중요. 기본값 없는 파라메터가 먼저 정의되어야 함
def f1(c, a=1, b=2):
    print(c, a, b)

f1(1)
f1(1,2)
