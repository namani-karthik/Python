import socket
host='localhost'
port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

msg=s.recv(1024)

while(msg):
    print('Received:'+msg.decode())
    msg=s.recv(1024)
s.close
