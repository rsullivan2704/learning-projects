import socket
# Create a socket and connect to a server
# Clients only create and connect
# No need to bind or listen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))

# send and receive some data
sock.sendall(b'test')
data = sock.recv(1024)
print(data.decode())
