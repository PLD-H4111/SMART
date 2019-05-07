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



HOST_NAME   = '0.0.0.0' #'127.0.0.1'
PORT_NUMBER = 80



# TODO: fix login enter key
# TODO: fix redirection in login





class HTTPHandler(BaseHTTPRequestHandler):
    """HTTPHandler
    
    This class is an handler for a HTTPServer, it handles GET requests
    
    Attributes:
        sessions: a dictionnary which contains the users' data
    """
    sessions = {}
    
    def __init__(self, request, client_address, server):
        """ constructor """
        self.actionServlet = action_servlet.ActionServlet()
        self.cookies = None
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        

    def set_headers(self, mimetype="text/html"):
        """ define the common headers for all the requests """
        self.send_response(200)
        #self.send_response(http.client.OK)
        self.send_header('Content-type', mimetype)
        self.send_header("Access-Control-Allow-Origin", "*")
        if self.cookies != None:
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
        self.set_headers()

    
    def do_GET(self):
        """ method: GET """
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
        
        # get the cookies
        self.cookieHeader   = self.headers.get('Cookie')
        self.cookies        = http.cookies.SimpleCookie( self.cookieHeader )
        
        ADMIN_PAGES = {"/admin.html", "/create_event.html"}
        AUTHENTICATION_PAGE = "login.html"
        MAIN_ADMIN_PAGE = "admin.html"
        INDEX_PAGE = "index.html"
        
        user_data = self._get_user_data()
        
        if path == "/":
            path = INDEX_PAGE
                    
        # Check file extension and set the right mime type
        sendReply = False
        mimetype = "text/html"
        for extension, type in mimetypes.items():
            if path.endswith(extension):
                mimetype = type
                sendReply = True
                break

        if not sendReply: # Forbidden
            path = "error403.html"
        print("user data avant admin pages", user_data)
        if path in ADMIN_PAGES:
            if user_data == None:
                path = AUTHENTICATION_PAGE
        # TODO: tester avec input_data
        try:
            f = open(os.curdir + os.sep + path, mode='rb')
            #self.sessions[ int(self.cookies["session-id"].value) ] = user_data
            self.set_headers(mimetype)
            self.wfile.write(f.read())#.encode())
            f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

                
    
    def do_POST(self):
        """ method: POST """

        print("\ndebut POST sessions", self.sessions)
        input_data = self.rfile.read( int(self.headers['Content-Length']) ).decode()    
        input_data = json.loads(input_data)
        print(input_data)
        
        path = urllib.parse.urlparse(self.path).path
        
        # get the cookies
        self.cookieHeader   = self.headers.get('Cookie')
        self.cookies        = http.cookies.SimpleCookie( self.cookieHeader )
        
        user_data = self._get_user_data()
        
        if path=="/action_servlet":
            user_data, result = self.actionServlet.fetch(user_data, input_data)
            self.sessions[ int(self.cookies["session-id"].value) ] = user_data
            self.set_headers()
            #print(result)
            self.wfile.write(result.encode("utf8"))
        

    def _get_user_data(self):
        """ check if user_data in cookies, else init them """
        user_data = None
        print("self.cookieHeader:", self.cookieHeader)
        print("self.cookies:", self.cookies)
        print("sessions: ", self.sessions)
        if (self.cookieHeader == None                   or # no cookie at all
                "session-id" not in self.cookies        or # no session-id in the cookies
                int(self.cookies["session-id"].value) not in self.sessions ): # wrong session-id
            #sesskey = base64.b64encode( os.urandom(32) ) #.decode("utf8")
            sesskey = int( random.random()*(10**10) )    # get a sess id
            self.cookies["session-id"]    = sesskey        # set the sess id in the cookies
        else:
            user_data = self.sessions[ int(self.cookies["session-id"].value) ]
        return user_data



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


