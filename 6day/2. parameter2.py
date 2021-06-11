def f1(*x): #가변인자. 튜플로 받아옴
    print('함수시작')
    for i in x:
        print(i)
    print('함수 끝')

def add(*num):
    s = 0
    for i in num:
        s+=i
    return s

def main():
    f1()
    f1('aaa', 'bbb')
    f1('ccc','ddd','eee','fff')

    s=add(1,2,3)
    print('add(1,2,3):',s)
    s=add(1,2,3,4,5)
    print('add(1,2,3,4,5):', s)
main()

