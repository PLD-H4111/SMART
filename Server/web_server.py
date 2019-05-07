#!/usr/bin/python3
# -*- coding: utf-8 -*-



from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv        # args passed when called the script
import http.cookies

import random
import base64
import os                    # curdir, sep

import socketserver
import json
import time
import cgi
import urllib.parse

from importlib import reload
import sys
sys.path.insert(0, './servlets/')
reload(sys)
import action_servlet



HOST_NAME          = '127.0.0.1'
PORT_NUMBER          = 80



class HTTPHandler(BaseHTTPRequestHandler):
    """HTTPHandler
    
    This class is an handler for a HTTPServer, it handles GET requests
    
    Attributes:
        sessions: blabla
    """
    # attr1 = 0 
    
    def __init__(self, request, client_address, server):
        self.sessions = {}
        self.actionServlet = action_servlet.ActionServlet()
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        

    def _set_headers(self):
        """ define the common headers for all the requests """
        self.send_response(200)
        #self.send_response(http.client.OK)
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        # set the cookies
        #self.send_header('Cookie', self.cookieHeader)
        #self.send_header('Set-Cookie', list(self.cookies.values())[i].output(header=''))
        ###self.send_header('Set-Cookie', self.cookies.output(header=''))
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
        
        # get the cookies
        self.cookieHeader    = self.headers.get('Cookie')
        self.cookies        = http.cookies.SimpleCookie( self.cookieHeader )
        
        path = urllib.parse.urlparse(self.path).path
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        #input_data            = self.rfile.read( int(self.headers['Content-Length']) )
        #print("path", path)
        #print("params", params)
        #print("input", self.headers)#['Content-Length'])#input_data)
        
        ADMIN_PAGES = {"/admin.html"}
        AUTHENTIFICATION_PAGE = "login.html"
        INDEX_PAGE = "index.html"
        
        if path=="/action_servlet":
            result = self.actionServlet.fetch(params)
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(result.encode("utf8"))
        else:
            if path == "/":
                path = INDEX_PAGE
                        
            # Check file extension and set the right mime type
            sendReply = False
            for extension, type in mimetypes.items():
                if path.endswith(extension):
                    mimetype = type
                    sendReply = True
                    break

            if sendReply == True:
                # Open the static file requested and send it
                try:
                    if path in ADMIN_PAGES:
                        user_data = self._get_user_data()
                        if user_data == None:
                            path = AUTHENTIFICATION_PAGE
                    # TODO: tester avec params
                        
                    f = open(os.curdir + os.sep + path, mode='rb')
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())#.encode())
                    f.close()
                except IOError:
                    self.send_error(404,'File Not Found: %s' % self.path)
            else: # acces non autorisé
                self.send_error(403,'The access tp "%s" is forbidden' % self.path)
        return

    def _get_user_data(self):
        """ check if user_data in cookies, else init them """
        user_data = None
        print("self.cookieHeader:\n", self.cookieHeader)
        print("self.cookies:\n", self.cookies)
        if (self.cookieHeader == None                   or # no cookie at all
                "session-id" not in self.cookies        or # no session-id in the cookies
                int(self.cookies["session-id"].value) not in self.sessions ): # wrong session-id
            #sesskey = base64.b64encode( os.urandom(32) ) #.decode("utf8")
            sesskey = int( random.random()*(10**10) )    # get a sess id
            self.cookies["session-id"]    = sesskey        # set the sess id in the cookies
        else:
            user_data = self.sessions[ int(self.cookies["session-id"].value) ]
        return user_data
        
        
    def do_POST(self):
        """ method: POST """
        
        """
        # get the cookies
        self.cookieHeader    = self.headers.get('Cookie')
        self.cookies        = http.cookies.SimpleCookie( self.cookieHeader )
        
        user_data            = self._get_user_data()
        input_data            = self.rfile.read( int(self.headers['Content-Length']) )        
        input_data            = input_data.decode()
        
        user_data, json_req_result    = webApp.handle_request( user_data, input_data )
        self.sessions[ int(self.cookies["session-id"].value) ] = user_data
        encoded_response    = bytes( json_req_result, 'utf-8' )
        
        self._set_headers()
        self.wfile.write(encoded_response)
        """
        
        
        input_data            = self.rfile.read( int(self.headers['Content-Length']) )        
        input_data            = input_data.decode()
        
        print(input_data)
        
        encoded_response    = bytes( "bravo", 'utf-8' )
        
        self._set_headers()
        self.wfile.write(encoded_response)




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


