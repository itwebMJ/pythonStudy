emails = []
#이름을 등록하고 검색하는 함수(몇번방에 있다)

def addEmail():
    while True:
        email = input('이메일 입력 : ')
        #이메일 중복체크
        res = searchEmail(email)
        if res == None:
           break
        else:
            print('이미 등록된 이메일. 다시 입력하시오')
    emails.append(email)

def searchEmail(s_email):
    for idx, i in enumerate(emails):
        if i == s_email:
            return idx
#동일한 이메일이 있으면 인덱스를 반환. 없으면 None 반환`

def printEmail():
    email = input('검색할 이메일 입력 : ')
    idx = searchEmail(email)
    if idx == None :
        print('없는 이메일입니다.')
    else:
        print(idx, '번째 방에 있음', emails[idx])

def printAll():
    print('등록한 이메일 : ')
    for i in emails:
        print(i, end=', ')
    print()

def main():
    while True:
        menu = input('메뉴 입력(1. 이메일 입력, 2. 이메일 검색, 3. 이메일 리스트출력 4. 종료) :')
        if menu == '1' :
            addEmail()
        elif menu =='2' :
            printEmail()
        elif menu =='3' :
            printAll()
        elif menu =='4' :
            break
main()