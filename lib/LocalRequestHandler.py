import os
from BaseHTTPServer import BaseHTTPRequestHandler

class LocalRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/"):
                f = open(self.server.docroot + os.sep + "index.html") 
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            elif self.path.endswith(".html"):
                f = open(self.server.docroot + os.sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            elif self.path.endswith(".xml"):
                #f = open(os.curdir + os.sep + self.path) 
                f = open(self.server.docroot + os.sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'text/xml')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            elif self.path.endswith(".css"):   #css
                # serve the css files from the base directory 
                f = open(self.server.base_dir + os.sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            elif self.path.endswith(".png"):   #css
                # serve the css files from the base directory 
                f = open(self.server.base_dir + os.sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            else:
                print "ends with '%s'" % self.path
                return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

