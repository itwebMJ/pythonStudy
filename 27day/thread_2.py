#클라이언트 프로그램
import socket, threading
members = []

soc = None
def sendMsg():
    while True:
        msg = input('msg:')
        soc.sendall(msg.encode(encoding='utf-8'))

        if msg=='/end':
            break

def recvMsg():
    while True:
        data = soc.recv(100)
        msg = data.decode()#읽은 데이터 디코딩
        print(msg)
        if msg=='/end':
            break
    soc.close()

def main():
    global  soc
    server_ip = '192.168.35.40'
    server_port = 3334

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((server_ip, server_port))  # 서버 accept()에 연결요청

    th1 = threading.Thread(target=sendMsg)
    th1.start()

    th2 = threading.Thread(target=recvMsg)
    th2.start()

    print('main 종료')


main()