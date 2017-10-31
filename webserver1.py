import socket
import time
from hello import app
import StringIO
import sys

env = {}

def start_response(status, response_headers):
    print status
    print response_headers

def respond_to_connection(client_connection):
    request = client_connection.recv(1024)
    print request
    request_method, request_path, request_version = request.splitlines()[0].strip().split()
    env['REQUEST_METHOD'] = request_method
    env['PATH_INFO'] = request_path
    env['wsgi.input'] = StringIO.StringIO(request)
    res = app(env, start_response)
    #for obj in res:
    #    print obj
    http_response = """\
HTTP/1.1 200 OK

"""
#Hello, World!
#"""
    http_response = http_response + "\n".join(res)
    client_connection.sendall(http_response)
    #time.sleep(60)
    client_connection.close()


def serve_forever(listen_socket):
    while True:
        client_connection, client_address = listen_socket.accept()
        respond_to_connection(client_connection)


if __name__ == "__main__":
    HOST, PORT = '', 8888

    env['wsgi.version']      = (1, 0)
    env['wsgi.url_scheme']   = 'http'
    #env['wsgi.input']        = StringIO.StringIO(self.request_data)
    env['wsgi.errors']       = sys.stderr
    env['wsgi.multithread']  = False
    env['wsgi.multiprocess'] = False
    env['wsgi.run_once']     = False
    # Required CGI variables
    #env['REQUEST_METHOD']    = self.request_method    # GET
    #env['PATH_INFO']         = self.path              # /hello
    env['SERVER_NAME']       = HOST       # localhost
    env['SERVER_PORT']       = str(PORT)  # 8888

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print 'Serving HTTP on port %s ...' % PORT
    serve_forever(listen_socket) 
