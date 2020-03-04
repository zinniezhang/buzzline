##!/usr/bin/python
#from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
from getNews import graphTicker
#import os
#
#
#PORT_NUMBER = 8080
#
##This class will handles any incoming request from
##the browser 
#class myHandler(BaseHTTPRequestHandler):
#	
#	#Handler for the GET requests
#	
#	def do_GET(self):
#		self.send_response(200)
#		self.send_header('Content-type','text/plain')
#		self.end_headers()
##		message = cow.Cowacter().milk('Hello from Python from a ZEIT Now Serverless Function!')
#		message = graphTicker(self.path[1:])
#		self.wfile.write(message.encode())
#		return
#
##	def do_GET(self):
##		self.wfile.write(bytes("hello", "utf-8"))
##		self.wfile.close()
##		return
##		print(self.path[1:])
##		self.send_header('Content-Type', 'text/plain')
##		self.end_headers()
##		if False: # os.path.exists(self.path[1:]):
###			with open(self.path[1:], 'rb') as f:
###				self.send_response(200)
###				if self.path.split('.')[1] == 'png':
###					self.send_header('Content-Type', 'image/png')
###				if self.path.split('.')[1] == 'html':
###					self.send_header('Content-Type', 'text/html')
###				if self.path.split('.')[1] == 'css':
###					self.send_header('Content-Type', 'text/css')
###				if self.path.split('.')[1] == 'jpg' or self.path.split('.')[1] == 'jpeg':
###					self.send_header('Content-Type', 'image/jpeg')
###				self.end_headers()
###				self.wfile.write(f.read())
###		# Send the html message
##			print("hi")
##		elif self.path == '/favicon.ico':
##			self.send_response(404)
##		else:
##			self.wfile.write(bytes('http://localhost:8080/' + graphTicker(self.path[1:]), 'utf-8'))
##		return
#
#try:
#	#Create a web server and define the handler to manage the
#	#incoming request
#	server = HTTPServer(('127.0.0.1', PORT_NUMBER), myHandler)
#	print('Started httpserver on port ' , PORT_NUMBER)
#	
#	#Wait forever for incoming htto requests
#	server.serve_forever()
#
#except KeyboardInterrupt:
#	print('^C received, shutting down the web server')
#	server.socket.close()

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__,static_url_path='/images', static_folder="stocks")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/<stock>')
@cross_origin()
def hello_world(stock):
    return jsonify(url = "http://localhost:5000/" + graphTicker(stock))


#@app.route("/images")
#@cross_origin()
#def return_image():
	

if __name__ == '__main__':
    app.run(debug=True)


	