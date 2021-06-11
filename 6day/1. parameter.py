def f1(name, tel, age=5):#age=5: 아규먼트 기본값
    print('name :',name)
    print('tel :', tel)
    print('age :', age+10)

def main():
    n = 'aaa'
    t = '1234'
    a = 12
    f1(tel=t, name=n, age=a)
    f1(n, t)
main()
