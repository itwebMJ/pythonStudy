'''
파일의 읽고 쓰기 위치 제어
tell() : 현재 위치 반환
seek(off, whence)
    :whence를 기준으로 off만큼 떨어진 위치로 이동, whence는 0(앞), 1(현재위치), 2(맨뒤)

ex>
abasdfad

ab
련재 : 2

seek(5, 0)
seek(-1, 1)
seek(-10, 2)

'''

def writeFile():
    f = open('./file/f.txt', 'w')
    s = 'abcdefghijklmnopqrstuvwxyz'
    f.write(s)
    f.close()

def readFile():
    f = open('./files/f.txt', 'rb')
    s = f.read(3)#3바이트 읽음
    print(s)
    print('현재위치:', f.tell())
    f.seek(5, 1)
    print('현재위치:', f.tell())
    s = f.read(1)
    print('현재 위치에서 5이동:', s)

    f.seek(-2, 1)
    s = f.read(1)
    print('현재 위치에서 -2이동:', s)
    f.seek(10, 0)
    s = f.read(1)
    print('맨앞에서 10이동:', s)
    f.seek(-1, 2)
    s = f.read(1)
    print('맨뒤에서 -1이동:', s)

    f.close()

def main():
    writeFile()
    readFile()

main()