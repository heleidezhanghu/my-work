import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = ('0.0.0.0', 5200)
server.bind(server_addr)
server.listen()
while 1:
    try:
        conn, conn_addr = server.accept()
        a = conn.recv(655535)
        # a = a.decode()
        # a.split('\n')
        print(a)
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n Hello,world!')
    except Exception:
        break
server.close()