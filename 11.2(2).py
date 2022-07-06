import socket 
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
port = 50005
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
msg = sock.recv(1024)
msg_decoded=msg.decode('utf-8')
msg_decoded