import socket
from threading import Thread
c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_addr = ('0.0.0.0', 5251)
c1.connect(s_addr)
def hehe():
    a = c1.recv(65535)
    return a
while 1:
    t = Thread(target=hehe)
    n = t.start()
    print(n)
    c1.send(input('请输入消息').encode())

