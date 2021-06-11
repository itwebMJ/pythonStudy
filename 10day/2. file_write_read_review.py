'''
입출력
입력: 밖에서 프로그램으로 데이터 들어오는 것. input():키보드로 입력받은 값이 프로그램으로 들어옴
출력: 프로그램에서 외부로 데이터가 나가는 것. print():프로그램 데이터가 콘솔로 나감
<표준입출력>. => 특별한 작업 없이 기본적으로 입력, 출력 할 수 있도록 기본 제공 입출력 객체
표준입력: sys.stdin => 표준입력장치(키보드)에서 읽음 담당
표준출력: sys.stdout => 표준출력장치(콘솔)에서 출력 담당
표준에러: sys.stderr => 표준출력장치(콘솔)에서 에러 출력 담당

읽기: sys.stdin.read(): 키보드 입력
쓰기: sys.stdout.write(): 콘솔 출력
에러출력: sys.stderr.write(): 콘솔에 에러 출력

<파일 입출력>
1. 파일 오픈
f = open('파일경로', '오픈모드') : 오픈모드(r:읽기, w:쓰기, a:이어쓰기). 반환값:오픈된 파일을 제어할 수 있는 file 객체

2. 읽고, 쓰기
f.read():파일 읽기
f.write():쓰기

3. 파일 닫음
f.close()
'''

import sys, os

def stdTest():
    msg = sys.stdin.readline() #표준입력(키보드)로 한줄 읽기
    sys.stdout.write('msg:'+msg+'\n') #표준출력(콘솔)로 한줄 출력
    sys.stderr.write('에러 메시지 출력\n') #표준에러로 에러 출력

def fileRead(path):
    try:
        f = open(path, 'r', encoding='utf-8') #파일오픈
        x = f.read()  #파일읽기. 파일에서 읽은 내용 반환 => 변수 x에 저장
        print(x)  #x(파일에서 읽은 내용) 출력
        f.close()           #파일닫기

    except Exception as e:
        print(e)

def fileWrite(path, msg):
    try:
        f = open(path, 'w', encoding='utf-8') #쓰기모드 파일 오픈
        f.write(msg)#파일에 쓸 내용
        f.close()
    except Exception as e:
        print(e)

def printDirList(path):#10day
    if not os.path.isdir(path):#디렉토리 존재를 True, False로 반환
        print('없거나 디렉토리가 아님')
        return

    fname = os.listdir(path)#path 폴더에 있는 모든 파일이나 디렉토리 이름(문자열)을 모두 읽어서 리스트에 담아서 반환
            #path가 10day: ['a.txt', 'b.txt', '입출력.py', '3. call_package.py']
    for file in fname:
        print(file)

def main():
    #stdTest()
    #fileWrite('b.txt', 'hello file\n')
    #fileRead('b.txt')
    printDirList('./')

main()