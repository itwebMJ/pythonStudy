def write1():
    file = open('./file/b.txt', 'w', encoding='utf-8')
    file.write('hello file')
    file.close()

def write2():
    file = open('./file/c.txt', 'w', encoding='utf-8')
    while True:
        s = input('메시지 입력(멈추려면 /stop):')
        if s=='/stop':
            break
        else:
            file.write(s+'\n')
    file.close()

def copy(src, dest):#파일복사
    f1 = open(src, 'r', encoding='utf-8')
    f2 = open(dest, 'w', encoding='utf-8')
    data = f1.read()
    f2.write(data)
    f1.close()
    f2.close()

def main():
    # write1()
    write2()

    copy('./file/a.txt', './file/d.txt')

main()


