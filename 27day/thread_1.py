#클라이언트 프로그램
import socket

server_ip = '192.168.35.40'
server_port = 3333

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))

while True:
    msg = input('msg:')
    socket.sendall(msg.encode(encoding='utf-8'))

    #서버가 에코로 되돌려보낸 메시지 받음
    data = socket.recv(100)
    msg = data.decode()#읽은 데이터 디코딩
    print('echo msg:', msg)
    if msg=='/end':
        break

socket.close()