import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'<Vlad krutoy!>', ('127.0.0.1', 8888))