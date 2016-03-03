import json
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class krakeHandler(BaseHTTPRequestHandler):
  
  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','application/json')
    self.end_headers()
    # Send the html message
    info = dict()
    info["something"] = "wong"
    info["cant_do"] = "much"
    self.wfile.write( json.dumps( info ) )
    return

  #Handler for the POST requests
  def do_POST(self):
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.send_header('Content-type','application/json')
    self.end_headers()

    data = json.loads(self.data_string)
    self.wfile.write( json.dumps( data ) )
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), krakeHandler)
  print 'Started httpserver on port ' , PORT_NUMBER
  
  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print '^C received, shutting down the web server'
  server.socket.close()
  