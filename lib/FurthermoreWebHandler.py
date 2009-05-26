import os
from BaseHTTPServer import BaseHTTPRequestHandler

class FurthermoreWebHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                f = open(os.curdir + os.sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".css"):   #css
                print "Opening css file '%s/%s'" % \
                        (os.curdir, self.path)
                f = open("%s/" % os.curdir + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
                
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

