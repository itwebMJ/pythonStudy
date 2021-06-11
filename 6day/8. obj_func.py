'''
함수 객체
함수를 변수에 담음


def f1(name):
    print(name, ' hello')

def main():
    #obj => 함수 객체
    obj = f1  #함수이름에는 함수 참조값이 있다
    obj('aaa')

main()
'''
'''
1. 핸들러로 활용: 함수를 다이렉트로 호출하지 않고 이벤트 핸들러로 등록해서 사용하고자 할때 사용할 수 있다

def onEvent(f):
    print('이벤트 등록')
    f()#함수 객체로 함수 대신 호출

def handler():
    print('3의 배수')

def main():
    for i in range(1, 30):
        print(i)
        if i%3==0:
            onEvent(handler)
main()
'''
'''
2. 룩업테이블(리스트): 함수를 리스트에 담고 제어문 대신 인덱스를 활용해서 함수를 호출하면 성능향상을 볼 수 있음
'''
'''

def 밥먹기():
    print('피카추 밥먹음')

def 잠자기():
    print('피카추 잠자기')

def 놀기():
    print('피카추 놀기')

def 운동하기():
    print('피카추 운동하기')

def main():
    funcs = [밥먹기, 잠자기, 놀기, 운동하기]
    menu = int(input('1.밥먹기 2.잠자기 3.놀기 4운동하기'))
    funcs[menu-1]()

main()
'''
'''
함수이용하여 주소록 만들기
한사람정보(이름,전화번호,주소)
1. 등록(이름중복안됨)
2. 검색(이름으로) => 정보출력. 없다
3. 수정(이름으로) => 전화, 주소 수정
4. 삭제(이름으로 )
5. 전체출력
6. 종료
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