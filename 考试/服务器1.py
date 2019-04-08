import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 41900)
server.bind(server_addr)
print('服务器已经开启')
server.listen(10)
def recv(conn, conn_addr):
    while 1:
        try:
            msg = conn.recv(1460)
            print('收到消息', msg.decode())
            conn.send('消息已经收到了'.encode())
        except Exception:
            break
while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break
    t = Thread(target=recv,args=(conn, conn_addr))
    t.start()
server.close()
print('服务器已经结束')
