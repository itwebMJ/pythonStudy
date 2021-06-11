def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def nanugi(x, y):
    if y != 0:
        return x / y

num1 = int(input('num1 :'))
input_data = input('연산자 :')
num2 = int(input('num2 :'))
result = None
'''
print(num1, '+', num2, '=', add(num1,num2))
print(num1, '-', num2, '=', minus(num1,num2))
print(num1, '*', num2, '=', multiple(num1,num2))
res = nanugi(num1,num2)
'''
'''
if result == 'None':
    print('0으로 나눌 수 없음')
else :
    print(num1, '/', num2, '=', res)
'''
if(input_data == '+'):
    result = add(num1, num2)
elif(input_data == '-'):
    result = minus(num1, num2)
elif(input_data == '*'):
    result = multiple(num1, num2)
elif(input_data == '/'):
    if num2 != 0:
        result = nanugi(num1, num2)
if result == None:
    print('잘못 입력 했습니다(+, -, *, / 중 입력)')
else :
    print(num1, input_data, num2, '=', result)