import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((' 172.16.1.230' , 60917)) #our own IP Adress
s.listen(5)
clinetsocket , clientaddress = s.accept()
print(clinetsocket) #first step
clientaddress()
print('Got a connection from %s'%str(clientaddress))
msg = input('Enter any Message:')
msg_encoded=msg.endcode('utf-8')
clinetsocket.send(msg_encoded)