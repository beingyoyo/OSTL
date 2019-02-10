import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")

port = 10101

s.bind(('localhost',port))

s.listen(5)

msg = "You are connected"
print("Waiting for connection")

while True:
	
	conn,addr = s.accept()

	print("Connected to",addr)

	conn.send(msg.encode())

	print(conn.recv(100).decode())

	conn.close()

	print("Connection closed")