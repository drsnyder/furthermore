# vim: set expandtab textwidth=79 ts=4 sts=4 ft=python:
# add another class to handle what main is doing below
import os
from BaseHTTPServer import HTTPServer
from FurthermoreWebHandler import *

class LocalHTTPServer(HTTPServer):

    def __init__(self, base_dir, out_dir, host='', port=8080):
        HTTPServer.__init__(self, (host, port), FurthermoreWebHandler)
        self.base_dir = base_dir
        self.docroot = out_dir
        self.port = port

    def run(self):
        try:
            print 'started http server on %d...' % self.port
            self.serve_forever()
        except KeyboardInterrupt:
            print '^C received, shutting down server'
            self.socket.close()


