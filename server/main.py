# This file is the entrypoint of the server and registers the listener and request handler
from HttpHandler import Handler
from BaseHTTPServer import HTTPServer

PORT_NUMBER = 8080

try:
    Handler.server_version = ''
    Handler.sys_version = ''
    server = HTTPServer(('', PORT_NUMBER), Handler)
    print('Started httpserver on port ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
