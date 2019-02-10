import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 10101

s.connect(('localhost',port))

print(s.recv(100).decode())

msg = "Message received"

s.send(msg.encode())

s.close()


'''OUTPUT:
comp@comp-HP:~/Desktop$ python3 server.py 
Socket created
Waiting for connection
Connected to ('127.0.0.1', 46632)
Message received
Connection closed

comp@comp-HP:~/Desktop$ python3 client.py 
You are connected

'''