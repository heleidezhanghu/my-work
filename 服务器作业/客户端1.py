import os
import socket
#__file__的意思的是 本python文件在os中的绝对路径
# os.path.dirname 的意思是找到文件所属的文件夹名称
# os.path.join的意思是拼凑文件的路径,并且可以在windows linux系统之间动态的切换 文件分隔符 '/','\'

dir_name = os.path.dirname(__file__)
# jpg_name = dir_name + '/' + '3_1.jpeg'

png_name = os.path.join(dir_name, '11.png')

with open(png_name, 'rb') as f:
    b_file = f.read()

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('127.0.0.1',60000)

ss.connect(addr)

ss.sendall(b_file)

ss.close()
