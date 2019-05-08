#!/usr/bin/python3
# -*- coding: utf-8 -*-



from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv        # args passed when called the script
from http import HTTPStatus
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
# TODO: fix sessions with posts
# TODO: error403 must send 403 code
# TODO: créer une session seulement si on en a besoin
# TODO: gérer la deconnexion et mieux gérer les cas limites de reconnexion





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
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        

    def set_headers(self, mimetype="text/html", cookies=None):
        """ define the common headers for all the requests """
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', mimetype)
        self.send_header("Access-Control-Allow-Origin", "*")
        if cookies != None:
            self.send_header('Set-Cookie', cookies.output(header=''))
        self.end_headers()


    def do_OPTIONS(self):
        """ method: OPTIONS """
        self.send_response(HTTPStatus.OK)
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
            '.js': "application/javascript",
            '.json': "application/json"
        }
        
        path = urllib.parse.urlparse(self.path).path
        
        # get the cookies
        cookieHeader   = self.headers.get('Cookie')
        cookies        = http.cookies.SimpleCookie(cookieHeader)
        
        ADMIN_PAGES = {"/admin.html", "/create_event.html", "/event_details.html"}
        AUTHENTICATION_PAGE = "login.html"
        MAIN_ADMIN_PAGE = "admin.html"
        INDEX_PAGE = "index.html"
        
        user_data = self._get_user_data(cookieHeader, cookies)
        
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

        if path in ADMIN_PAGES:
            if user_data == None:
                path = AUTHENTICATION_PAGE
        # TODO: tester avec input_data
        try:
            f = open(os.curdir + os.sep + path, mode='rb')
            self.set_headers(mimetype, cookies)
            self.wfile.write(f.read())#.encode())
            f.close()
        except IOError:
            self.send_error(HTTPStatus.NotFound,'File Not Found: %s' % self.path)

                
    
    def do_POST(self):
        """ method: POST """

        print("\ndebut POST sessions", self.sessions)
        input_data = self.rfile.read( int(self.headers['Content-Length']) ).decode()    
        input_data = json.loads(input_data)
        print(input_data)
        
        path = urllib.parse.urlparse(self.path).path
        
        # get the cookies
        cookieHeader   = self.headers.get('Cookie')
        cookies        = http.cookies.SimpleCookie(cookieHeader)
        
        user_data = self._get_user_data(cookieHeader, cookies)
        
        if path == "/action_servlet":
            user_data, result = self.actionServlet.fetch(user_data, input_data)
            
            if user_data != None:
                if "session-id" not in cookies:
                    self._create_session(user_data, cookies)

                self.sessions[int(cookies["session-id"].value)] = user_data

            self.set_headers("application/javascript", cookies)
            self.wfile.write(result.encode("utf8"))
        

    def _get_user_data(self, cookieHeader, cookies):
        """ check if user_data in cookies, else init them """
        user_data = None
        if cookieHeader != None and "session-id" in cookies:
            session_id = int(cookies["session-id"].value)
            if session_id in self.sessions:
                user_data = self.sessions[int(cookies["session-id"].value)]
            else:
                del cookies["session-id"]
        return user_data

    def _create_session(self, user_data, cookies):
        """ """
        #sesskey = base64.b64encode( os.urandom(32) ) #.decode("utf8")
        sesskey = int( random.random()*(10**10) )     # get a sess id
        cookies["session-id"] = sesskey               # set the sess id in the cookies
        return 


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


