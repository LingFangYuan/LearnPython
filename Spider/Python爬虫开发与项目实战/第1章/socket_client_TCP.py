import socket

# 初始化socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接目标的IP和端口
s.connect(('172.30.196.154', 8001))

# 接收消息
print('--->'+s.recv(1024).decode('utf-8'))

# 发送消息
s.send(b'Hello, I am client')
print('--->'+s.recv(1024).decode('utf-8'))
s.send(b'exit')

# 关闭连接
s.close()