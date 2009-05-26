# vim: set expandtab textwidth=79 ts=4 sts=4 ft=python:
# add another class to handle what main is doing below
import os
from BaseHTTPServer import HTTPServer
from FurthermoreWebHandler import *

class LocalHTTPServer:

    def __init__(self, port=8080, dir="%s/../out/" % os.path.dirname(__file__)):
        # I'm not crazy about how this currently works. I have to copy the css
        # directory from the base to the dir specified here before we begin
        # serving files
        self.dir = dir
        self.port = port
        self.server = HTTPServer(('', self.port), FurthermoreWebHandler)

    def run(self):
        os.chdir(self.dir)
        try:
            print 'started http server on %d...' % self.port
            self.server.serve_forever()
        except KeyboardInterrupt:
            print '^C received, shutting down server'
            self.server.socket.close()


