from CGIHTTPServer import CGIHTTPRequestHandler
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from os import curdir, sep

''' simple web server
'''
class RedirectHandler(BaseHTTPRequestHandler)

  def do_GET(self):
    ''' get handler
    '''
    print self.headers
    try:
      if self.path.endswith(".html"):
        f = open(curdir + sep + self.path) #self.path has /test.html
        #note that this potentially makes every file on your computer readable by the internet
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()
        return
    except IOError:
      self.send_error(404,'File Not Found: %s' % self.path)

  def do_POST(self):
    ''' post handler
    '''
    #cookiestring = "\n".join(self.headers.get_all('Cookie',failobj=[]))
    print self.headers
    self.send_response(200)
    self.send_header("Content-type", "json")
    self.send_header("Set-Cookie", "pageAccess=3")
    self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8000')
    self.send_header('Access-Control-Allow-Credentials', 'true')
    self.end_headers()
    self.wfile.write('{"post":"true"}')

if __name__ == '__main__':
  server_address=('',7777)
  httpd = HTTPServer(server_address, RedirectHandler)
  httpd.serve_forever()
