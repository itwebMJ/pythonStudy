
class Member:
    def __init__(self, id, pwd, name='아무개', email='이메일'):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printMember(self):
        print('id', self.id)
        print('ped', self.pwd)
        print('name', self.name)
        print('email', self.email)

def main():
    m1 = Member('tt','2222','aaa', 'asdaf')
    print('===m1====')
    m1.printMember()

    m2 = Member(name='nameb', email='bbb@email.com', pwd='222', id='bbb')
    print('===m2====')
    m2.printMember()

    m3 = Member('ccc', '333')
    print('===m3====')
    m3.printMember()

    m4 = m3
    m4.name = '가나다'
    m4.email = '가나다@email.com'
    print('===m4====')
    m4.printMember()
    print('===m3====')
    m3.printMember()
main()
'''       
person = []
def addPerson():
    data = []
    while True:
        name = input('이름 입력 : ')
        #이름 중복체크
        i, idx = searchName(name)

        if i != -1 and idx != -1:
            print('이미 등록된 이름. 다시 입력하시오')
        else:
           break
    tel = input('전화번호 입력 : ')
    addr = input('주소 입력 : ')
    data.append(name)
    data.append(tel)
    data.append(addr)

    person.append(data)

def searchName(s_name):
    idx = 0
    cnt = 0

    for i in range(0, len(person)):
        for j in range(0, len(person[i])):
            if person[i][j] == s_name:
                cnt+=1
                return i, j #person[i][idx]
            #idx +=1
    if cnt <= 0 :
        return -1, -1

def updatePerson():
    name = input('검색할 이름 입력 : ')
    global person

    i, idx = searchName(name)
    if i >-1  and idx > -1:
        #for i in person:
          #  for j in person[i]:
        #person[i][idx] = name
        tel = input('전화번호 입력 : ')
        addr = input('주소 입력 : ')
        person[i][idx+1] = tel
        person[i][idx+2] = addr
        print('이름 : ', name, '전화번호 : ', tel, '주소 : ',addr)
        print('수정 완료')
    else:
        print('없는 이름입니다.')

def printPerson():
    name = input('검색할 이름 입력 : ')
    i, idx = searchName(name)

    if i >-1  and idx > -1:
        print(i, '번째줄', idx, '번째 방에 있음', person[i][idx])
    else:
        print('없는 이름입니다.')

def printAll():
    print('등록한 사람 : ')
    for i in range(0, len(person)):
        for j in range(0, len(person[i])):
            print(person[i][j], end=', ')
        print()
    print()

def main():
    while True:
        menu = input('메뉴 입력(1. 이름 입력, 2. 이름 검색, 3. 수정, 4.출력, 5. 종료) :')
        if menu == '1' :
            addPerson()
        elif menu =='2' :
            printPerson()
        elif menu =='3' :
            updatePerson()
        elif menu =='4' :
            printAll()
        elif menu =='5' :
            break
main()
'''