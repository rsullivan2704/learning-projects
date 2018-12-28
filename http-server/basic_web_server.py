import socket

# Create HOST, PORT pair
HOST, PORT = '', 8888

# Create the socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set socket options
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to HOST, PORT pair
listen_socket.bind((HOST, PORT))
# Start listening for requests
listen_socket.listen(1)

print('Serving HTTP on port {port} ...'.format(port=PORT))
while True:
    # Accept the client request socket
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    # Build a response
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # Send the response
    client_connection.sendall(http_response)
    # Close the connection
    client_connection.close()