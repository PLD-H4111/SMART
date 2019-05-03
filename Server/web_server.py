#!/usr/bin/python3
# -*- coding: utf-8 -*-



from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv		# args passed when called the script
import http.cookies

import random
import base64
import os					# curdir, sep

import socketserver
import simplejson
import json
import time
import cgi
import urllib.parse

from importlib import reload
import sys
sys.path.insert(0, './servlets/')
reload(sys)
import action_servlet



HOST_NAME		  = '127.0.0.1'
PORT_NUMBER		  = 80





class HTTPHandler(BaseHTTPRequestHandler):
	"""HTTPHandler
	
	This class is an handler for a HTTPServer, it handles GET requests
	
	Attributes:
		sessions: blabla
	"""
	sessions = {}


	def _set_headers(self):
		""" define the common headers for all the requests """
		self.send_response(200)
		#self.send_response(http.client.OK)
		self.send_header('Content-type', 'text/html')
		self.send_header("Access-Control-Allow-Origin", "*")
		# set the cookies
		#self.send_header('Cookie', self.cookieHeader)
		#self.send_header('Set-Cookie', list(self.cookies.values())[i].output(header=''))
		self.send_header('Set-Cookie', self.cookies.output(header=''))
		self.end_headers()


	def do_OPTIONS(self):
		""" method: OPTIONS """
		self.send_response(200, "ok")
		self.send_header('Access-Control-Allow-Credentials', 'true')
		self.send_header('Access-Control-Allow-Origin', '*') # 'http://localhost:8888')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, HEAD, OPTIONS')
		self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
		self.end_headers()


	def do_HEAD(self):
		""" method: HEAD """
		self._set_headers()

		
	
	def do_GET(self):
		""" """
		mimetypes = {
			'.html': "text/html",
			'.css': "text/css",
			'.png': "image/png",
			'.gif': "image/gif",
			'.jpg': "image/jpeg",
			'.jpeg': "image/jpeg",
			'.ico': "image/x-icon",
			'.svg': "image/svg+xml",
			'.js': "application/javascript"
		}
		
		path = urllib.parse.urlparse(self.path).path
		params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
		#input_data			= self.rfile.read( int(self.headers['Content-Length']) )
		#print("path", path)
		#print("params", params)
		#print("input", self.headers)#['Content-Length'])#input_data)
				
		if path=="/action_servlet":
			result = action_servlet.fetch(params)
			self.send_response(200)
			self.send_header('Content-type', "text/html")
			self.end_headers()
			self.wfile.write(result.encode("utf8"))
		else:
			if path=="/":
				path="/index.html"
			try:
				# Check file extension and set the right mime type
				sendReply = False
				for extension, type in mimetypes.items():
					if path.endswith(extension):
						mimetype = type
						sendReply = True
						break

				if sendReply == True:
					# Open the static file requested and send it
					f = open(os.curdir + os.sep + path, mode='rb')
					self.send_response(200)
					self.send_header('Content-type', mimetype)
					self.end_headers()
					self.wfile.write(f.read())#.encode())
					f.close()
				return
			except IOError:
				self.send_error(404,'File Not Found: %s' % self.path)




def run(server_class=HTTPServer, handler_class=HTTPHandler, host=HOST_NAME, port=PORT_NUMBER):
	""" run the web server """
	server_address = (host, port)
	httpd = server_class(server_address, handler_class)
	print('Starting HTTP Server ...')

	print(time.asctime(), 'Server Starts - %s:%s' % (host, port))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt: # Ctrl + C
		pass
	httpd.server_close()
	print(time.asctime(), 'Server Stops - %s:%s' % (host, port))



if __name__ == "__main__":
	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()


