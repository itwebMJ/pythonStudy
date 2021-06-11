import calculation as calc     #패키지 파일에있는 모든 함수
#from calculation import add     #패키지 파일에서 add 함수 하나만 불러옴
import file_control as f
def main():
    res = calc.add(1,2)
    #res = add(1,2)
    print(res)

    res = calc.sub(1, 2)
    print(res)

    res = calc.mul(1, 2)
    print(res)

    res = calc.dev(1, 2)
    print(res)

    base_path = '../7day/file/'
    s = f.file_read(base_path+'a.txt')
    print('a file content : ', s)

    f.file_write(base_path+'b.txt', s)
    s = f.file_write(base_path+'b.txt', s)
    print('d file content : ', s)
main()