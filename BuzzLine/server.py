#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
from getNews import graphTicker
import os


PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if os.path.exists(self.path[1:]):
			with open(self.path[1:], 'rb') as f:
				self.send_response(200)
				if self.path.split('.')[1] == 'png':
					self.send_header('Content-Type', 'image/png')
				if self.path.split('.')[1] == 'html':
					self.send_header('Content-Type', 'text/html')
				if self.path.split('.')[1] == 'css':
					self.send_header('Content-Type', 'text/css')
				if self.path.split('.')[1] == 'jpg' or self.path.split('.')[1] == 'jpeg':
					self.send_header('Content-Type', 'image/jpeg')
				self.end_headers()
				self.wfile.write(f.read())
		# Send the html message
		elif self.path == '/favicon.ico':
			self.send_response(404)
		else:
			self.wfile.write(bytes('http://localhost:8080/' + graphTicker(self.path[1:]), 'utf-8'))
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