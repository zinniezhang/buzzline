#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
from getNews import graphTicker

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(bytes('http://localhost:8000/' + graphTicker(self.path[1:]), 'utf-8'))
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
    
import socketserver

PORT = 8000
web_dir = os.path.join(os.path.dirname(__file__), 'stocks')
os.chdir(web_dir)
Handler = SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()