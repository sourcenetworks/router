import errno
import os
import signal
import socket
import struct

from two1router.server import api

SERVER_ADDRESS = (HOST, PORT) = '', 9090
REQUEST_QUEUE_SIZE = 1024
SO_ORIGINAL_DST = 80

def free_proc(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)

    request_notify(request)

    http_response = b"""\
HTTP/1.1 200 OK
Date: Fri, 31 Dec 1999 23:59:59 GMT
Content-Type: text/plain
Content-Length: 4

meep
"""
    client_connection.sendall(http_response)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port}...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, free_proc)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
            data = client_connection.getsockopt(socket.SOL_IP,
                SO_ORIGINAL_DST, 16)

        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()
