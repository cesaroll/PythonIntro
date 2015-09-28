import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
    
Handler.protocol_version = Protocol

server_address = ('127.0.0.1', port)

httpd = Server(server_address, Handler)
#sa = httpd.socket.getsockname()
print("Serving HTTP")

httpd.serve_forever()
