# This implementation only works in Linux/MacOS since Windows doesn't implement os.fork()
# and the os.waitpid() function behaves differently

import errno
import os
import signal
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

# Handler method to wait to kill any child process
# until after it's parent process is killed
# Avoids zombie processes (status of process = Z+ with <defunct> in name)
# which happens when a child process is killed after it's parent
def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,             # Wait for any child process of the current process
                os.WNOHANG      # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return
        
        if pid == 0: # no more zombies
            return

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    # Build response
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # Send response
    client_connection.sendall(http_response)

def serve_forever():
    # Create socket, bind and start listening
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    # Handle the SIGCHLD event when a child process exits
    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            # Accept the client connection
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            if code == errno.EINTR:
                # restart 'accept' if it was interrupted
                # This happens when the parent process is blocked during the accept call
                # when the child process exits. The exit causes the SIGCHLD event that
                # is handled by the grim_reaper function. When the call to grim_reaper
                # is finished the accept call is interrupted
                continue
            else:
                raise
            
        pid = os.fork()
        if pid == 0: # chlid process
            listen_socket.close() # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0) # child exits here
        else: # parent
            client_connection.close() # close parent copy and loop over to continue processing new connections

if __name__ == '__main__':
    serve_forever()