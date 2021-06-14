class Person:
    def __init__(self):
        self.number = 0
        self.name = ''
        self.type = ''
        self.dept = ''

    def printInfo(self):
        print('number : ',self.number)
        print('name : ',self.name)
        print('type : ',self.type)
        print('dept : ',self.dept)

class Student(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.type = '학생'
        self.dept = dept
        self.stuSubj = []

    def applySub(self, sub):
        self.stuSubj.append(sub)

    def printApplySub(self):  #수강과목
        print('수강과목')
        for i in self.stuSubj:
            print(i)

class  Prof(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.type = '교수'
        self.dept = dept
        self.profSubj = []

    def lectureSub(self, sub):  #담당과목
        self.profSubj.append(sub)

    def printLectureSub(self):
        print('수강과목')
        for i in self.profSubj:
            print(i)
class Staff(Person):
    def __init__(self, number, name, dept) :
        super().__init__()
        self.number = number
        self.name = name
        self.type = '교직원'
        self.dept = dept
        self.job = ''

    def setJob(self, job):
        self.job = job

    def printJob(self):
        print('담당 직무 : ', self.job)

def main():
    s1 = Student(1, 'aaa', '컴퓨터공학')
    s1.applySub('전산학개론')
    s1.applySub('컴퓨터비전')
    s1.printInfo()
    s1.printApplySub()

    p1 = Prof(2, 'bbb', '전자공학')
    p1.lectureSub('C언어')
    p1.lectureSub('VHDL')
    p1.printInfo()
    p1.printLectureSub()

    s2 = Staff(3, 'ccc', 'HR')
    s2.setJob('인재양성')
    s2.printInfo()
    s2.printJob()
if __name__ == '__main__':
    main()