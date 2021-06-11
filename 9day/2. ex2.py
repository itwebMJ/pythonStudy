class Student:
    def __init__(self, name='', num=0, score=[]):
        self.name = name
        self.num = num
        self.score = score #[국영수총평] 담을 리스트

    def calc(self):
        for i in range(0, 3):
            self.score[3] += self.score[i]

        self.score[4] = self.score[3]/3

    def printInfo(self):
        print(self.name, end='\t')
        print(self.num, end='\t')
        for i in self.score:
            print(i, end='\t')
        print()

def main():
    s1 = Student('aaa', 1, [67,87,89,0,0])#객체 생성. 메모리 할당. 메모리 초기화.
    s1.calc()
    s1.printInfo()

    s2 = Student('bbb', 2, [67,93,59, 0, 0])  # 객체 생성. 메모리 할당. 메모리 초기화.
    s2.calc()
    s2.printInfo()
main()