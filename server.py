import socket
s=socket.socket()
s.bind(('localhost',9999))
s.listen(5)
c,addr=s.accept()
while True:
    ClientMsg=c.recv(1024).decode()
    c.send(ClientMsg.encode())