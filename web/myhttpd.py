# coding: utf-8

import wsgiref.simple_server

httpd = wsgiref.simple_server.make_server('', 8000, wsgiref.simple_server.demo_app)
print('start app on port 8000')
httpd.serve_forever()

