import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('0.0.0.0', 41900)
client.connect(server_addr)
while 1:
    try:
        client.send(input('请输入信息').encode())
        msg = client.recv(1460)
        print('收到服务器返回的消息', msg.decode())
        print('链接已经完成')
    except Exception:
        break
client.close()