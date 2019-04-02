import socket
from threading import Thread
def a(conn, conn_addr):
    while 1:
        a = conn.recv(65535).decode
        l1.append(a)
        print(l1)
        conn.send(l1[-1].encode())


# 把所有的消息放在一个列表里面

l1 = ['haha','hehe']
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = ('0.0.0.0', 5250)
server.bind(server_addr)
server.listen(3)
print('服务器已启动')
while 1:
    conn, conn_addr = server.accept()
    t = Thread(target=a, args=(conn, conn_addr))
    t.start()

