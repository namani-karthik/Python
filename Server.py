import socket
host='localhost'
port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#SOCK_DGRAM

s.bind((host,port))

s.listen(1)

c,addr=s.accept()

print('Connection from',str(addr))
c.send(b'I have accepted the connection')
c.send(b'Hello client, how are u')
msg='bye'
c.send(msg.encode())

c.close()
