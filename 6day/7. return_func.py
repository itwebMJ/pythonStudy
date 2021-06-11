'''
재귀함수
자신을 호출하는 함수
반복동작을 짧게 구현할 수있는 장점이 있지만 스택 사용량이 확 늘어나서 스택 오버플로우 문제 발생가능.
대부분 재귀는 루프로 대체 가능하기 때문에 루프로 대체하는 것이 좋다
'''

#5! = 5*4*3*2*1
def fact(num):
    if num==1:
        return 1
    else:
        return num * fact(num-1)

def fact2(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


def fibo1(num):
    if num <= 2:
        return 1
    else:
        return fibo1(num-1) +fibo1(num-2)

def fibo2(cnt):
    i, j, k = 1, 1, 0
    for x in range(1,cnt+1):
        if x < 3 :
            print(1, end='\t')
        else:
            k = i + j
            print(k, end='\t')
            i = j
            j = k

def fibo3(cnt):
    res = [1,1]
    for i in range(2, cnt+1):
        res.append(res[i-2]+res[i-1])
    return res

def main():
    '''
    for i in range(1, 101):
        print(fibo1(i))
    '''
    '''
    fibo2(50)
    print()

    res = fibo3(50)
    print(res)
    '''
    res = fact(5)
    print('5!:', res)

    res = fact2(4)
    print('4!:', res)

main()