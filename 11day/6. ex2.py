#다형성 구현. => 한 코드가 다양한 형태로 실행되는 것
class Car:
    def __init__(self):
        self.name = ''

    def horn(self):
        print('car - horn()')

class 소방차(Car):
    def __init__(self):
        super().__init__()
        self.name = '소방차'

    def horn(self):
        print('소방차 - horn()')

class 구급차(Car):
    def __init__(self):
        super().__init__()
        self.name = '구급차'

    def horn(self):
        print('구급차 - horn()')

class 경찰차(Car):
    def __init__(self):
        super().__init__()
        self.name = '경찰차'

    def horn(self):
        print('경찰차 - horn()')

def main():
    obj = None
    print('자동차를 선택하시오')
    s = input('1.소방차 2.구급차 3.경찰차')
    if s=='1':
        obj = 소방차()
    elif s=='2':
        obj = 구급차()
    elif s=='3':
        obj = 경찰차()
    else:
        obj = 소방차()

    print(obj.name)
    obj.horn()

main()