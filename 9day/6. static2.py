'''
문제
Test 클래스 만들고
객체가 생성되는 것을 카운팅하시오
'''

class Test:
    cnt = 0 #객체들이 공유해야 하는 값
    def __init__(self):
        Test.cnt += 1
        print(Test.cnt, '번째 객체 생성')

def main():
    for i in range(0, 5):
        Test()

main()