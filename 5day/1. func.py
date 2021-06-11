'''
def hello():
   print('hello')
hello()

def add(x, y):
    return x +y
res = add(1,2)
print(res)

def gugudan(dan):
    for i in range(2,10):
        print(dan,'*',i,'=',dan*i)
input_dan = int(input('구구단의 단을 입력 :'))
gugudan(input_dan)

for i in range(2, 10):
    gugudan(i)
'''

def add(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiple(x, y):
    return x * y
def nanugi(x, y):
    if y != 0:
        return x / y

'''
x = 6
y = 3
print(x, '+', y, '=', add(x,y))
print(x, '-', y, '=', minus(x,y))
print(x, '*', y, '=', multiple(x,y))
res = nanugi(x,y)
if res == 'none':
    print('0으로 나눌 수 없음')
else :
    print(x, '/', y, '=', nanugi(x,y))
'''

num1 = int(input('num1 :'))
num2 = int(input('num2 :'))
result = None

print(num1, '+', num2, '=', add(num1,num2))
print(num1, '-', num2, '=', minus(num1,num2))
print(num1, '*', num2, '=', multiple(num1,num2))
result = nanugi(num1,num2)

if result == None:
    print('0으로 나눌 수 없음')
else :
    print(num1, '/', num2, '=', result)

