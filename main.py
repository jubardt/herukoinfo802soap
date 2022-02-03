from wsgiref.simple_server import make_server
import os

from CarListService import wsgi_application

port = int (os.environ.get('PORT',8000))

server = make_server('0.0.0.0', port, wsgi_application)
print("server is running on port " + str(port))
server.serve_forever()
