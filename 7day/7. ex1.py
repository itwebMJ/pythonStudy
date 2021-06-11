'''
프로그램 시작되면 memo 디렉토리 없으면 새로 생성.(맨처음만)

메모장
1. 쓰기
    파일명 => 중복 : 덮어쓰기 : 기존 내용 지우고 작성
                    이어쓰기 : 기존 내용 살려서 뒤에 이어씀.        =>키보드로 내용입력('/exit':입력 멈춤) 파일에 씀 =>파일 닫고 종료
            새이름 : 새 파일 생성
2. 읽기
    memo 디렉토리의 파일 목록 출력 => 파일 선택 => 그 파일을 읽기 모드로 오픈해서 파일 내용 읽어와서 출력

3. 삭제
    memo 디렉토리의 파일 목록 출력 => 삭제할 파일 선택 => 선택한 파일 삭제
4. 종료
'''
import os

def init(path): #초기화 함수.
    if not os.path.isdir(path): #지정한 디렉토리 있나 확인하여 없으면
        os.mkdir(path)  #새로 생성

def selectFile(path): #파일 선택 함수.
    flist = os.listdir(path)  #메모 디렉토리의 파일 목록 읽어옴[a.txt, b.txt, c.txt]

    if len(flist)==0:
        print('파일이 없다')
        return

    print('메모 파일 목록')
    for i in range(0, len(flist)):#파일 목록 출력
        print(i, '. '+flist[i])  #인덱스. 파일명

    while True:
        idx = int(input('선택할 파일의 번호를 입력하시오'))
        if 0 <= idx <= len(flist)-1:
            break

    return flist[idx]

def readFile(path):
    fname = selectFile(path)
    if fname == None:
        return
    print('선택한 파일명:', fname)
    f = open(path+fname, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    print('===', fname, '내용===')
    print(content)

def nameCheck(path, fname): #파일 이름 중복 체크 및 중복됐을때 모드 선택. mode, 새파일명(중복됐을때 새로 입력받은 파일명)
    flist = os.listdir(path)  #메모 디렉토리 목록
    mode = 'w'      #디폴트 모드 w로 설정

    if len(flist)==0:
        return mode, ''

    newName = ''
    if fname in flist:  #in: 리스트에 in 앞의 값이 있으면 True, 없으면 False. fname이 중복된 이름
        newName = flist[0]
        x = int(input('1.덮어쓰기 2.이어쓰기 3.새파일명입력'))
        if x==1:
            mode = 'w'
            newName = ''
        elif x==2:
            mode = 'a'
            newName = ''
        elif x==3:
            while newName in flist: #중복되지 않는 이름을 입력할때까지 계속 입력받음
                newName = input('새파일명:')
        else:
            print('중복처리 중 잘못된 메뉴로 종료')
            return
    return mode, newName
    #반환값이 None이면 잘못된 입력 쓰기 중단
    #newName=='': mode값만 이용해서 쓰기작업
    #newName!='': 새파일명 입력했음

def writeFile(path):
    fname = input('파일명 입력')
    res = nameCheck(path, fname)
    mode = ''
    if res == None:
        print('파일 중복처리 선택을 잘못해서 여기서 끝냄')
        return
    elif res[1]=='':
        mode = res[0]
    elif res[1]!='':
        mode = res[0]
        fname = res[1]
    else:
        return

    f = open(path+fname, mode, encoding='utf-8')
    while True:
        msg = input('내용입력(멈추려면 /exit):')
        if msg=='/exit':
            break
        else:
            f.write(msg+'\n')
    f.close()

def main():
    memo_path = 'memo/'
    init(memo_path)
    while True:
        menu = input('1.읽기 2.쓰기 3.삭제 4.종료')
        if menu=='1':
            readFile(memo_path)
        elif menu=='2':
            writeFile(memo_path)
        elif menu=='4':
            break

main()