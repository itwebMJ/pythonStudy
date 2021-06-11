'''
파일 입출력
1. 파일 오픈
#   file = open(파일경로, 모드) #모드 기본값 r.
#   r(읽기. 파일 없으면 에러), w(쓰기. 파일이 없으면 새로 생성. 있으면 내용지우고 새로 생성), a(이어쓰기.있으면 내용 이어씀)
    t(텍스트), b(바이너리)
    rb 바이너리로 읽겠다
    r+(읽고 쓰기모드), w+(읽고 쓰기), a+(읽고 쓰기)
2. 읽기/쓰기 작업
읽기
    read(size) : size 크기만큼 파일에서 읽어서 반환
    read() : 파일 전체 읽어서 반환
    readLine() : 한 줄 읽어서 만환
쓰기
    write(출력값) : 파일에 출력 값을 씀
    writeLine(리스트, 튜플...) : 리스트나 튜플에 들어있는 값들을 파일에 출력

3. 파일 사용이 끝나면 파일 닫음
file. close()

<경로 표현>
1. 절대경로
    C:\\Users\\사용자 A\\PycharmProjects\\pythonProject\\7day\\file\\a.txt
2. 상대경로
    현재 프로그램을 기준으로 해당 파일 찾아감
    ./ 현재 디렉토리
    ../ 상위 디렉토리
    디렉토리명 => 하위 디렉토리

    ../file/a.txt
    ../../6day/1. parameter/py
'''
def read1():
    print('====read1====')
    file = open('./file/a.txt', 'r', encoding='utf-8') #encoding='utf-8' 한글 인코딩
    while True:
        s = file.read(5)#5바이트씩 읽기
        if s == '':#더이상 읽은것이 없을 때 멈춤
            break
        else:
            print(s, end='')
    file.close()
    print()

def read2():
    print('====read2====')
    file = open('./file/a.txt', 'r', encoding='utf-8')
    s = file.read()#한번에 전체 읽기
    print(s)
    file.close()

def read3():
    print('====read3====')
    file = open('./file/a.txt', 'r', encoding='utf-8')
    while True:
        s = file.readline()#한줄씩 읽기
        if s=='':
            break
        else:
            print(s)
    file.close()

def main():
    read1()
    read2()
    read3()

main()
