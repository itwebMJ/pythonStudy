def file_read(path):
    f = open(path, 'r', encoding='utf-8')   #파일 읽기 모드로 오픈
    s= f.read()     #파일 읽기
    f.close()       #파일  닫기
    return  s

def file_write(path, content):
    f = open(path, 'a', encoding='utf-8')   # 파일 이어쓰기 모드로 오픈
    f.write(content)     #파일 읽기
    f.close()       #파일  닫기



