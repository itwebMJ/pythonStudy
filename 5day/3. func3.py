def yaksu(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i, end='\t')
yaksu_num = int(input('약수를 구할 수 입력 :'))
yaksu(yaksu_num)
#print(yaksu(yaksu_num))
print()
def yaksu2(num):
    res=[]
    for i in range(1, num+1):
        if num % i == 0:
            res.append(i)
    return res
def yaksuPrint(data):
    print(data[len(data)-1], '의 약수: ', end='')
    for i in data:
        print(i, end=',')
    print()
x = int(input('num : '))
data2 = yaksu2(x)
yaksuPrint(data2)

def f1():
    print('파라메터, 리턴값 없는 함수')

def f2(num):
    print('입력받은 숫자:', num)

def f3(name, age):
    print('당신의 이름은:', name)
    print('당신의 나이는:', age)


def f4(name, age):
    msg = '당신의 이름은:'+name+', 당신의 나이는:'+str(age)
    return msg

def f5(name, age):
    return name, age  #리턴값이 여러개면 하나의 튜플로 반환됨

f1()
f2(3)
f3('aaa', 12)
s = f4('aaa', 12)
print(s)
#n, a = f5('bbb', 13)
#print(n, ':', a)
t = f5('bbb', 13) #t는 튜플
print(type(t))
print('name:',t[0], ', age:',t[1])