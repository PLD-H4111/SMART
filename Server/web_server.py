#!/usr/bin/python3
# -*- coding: utf-8 -*-



from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver, email.utils, datetime
from sys import argv        # args passed when called the script
from http import HTTPStatus
import shutil
import http.cookies

import random
import base64
import os                    # curdir, sep

import json
import time
import cgi
import urllib.parse

from importlib import reload
import sys
sys.path.insert(0, './database/')
sys.path.insert(0, './servlets/')
reload(sys)
import action_servlet

# For Python < 3.7 (instead of from http.server import ThreadingHTTPServer)
class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    daemon_threads = True


HOST_NAME   = '0.0.0.0' #'127.0.0.1'
PORT_NUMBER = 80



# TODO: fix sessions with posts
# TODO: error403 must send 403 code
# TODO: gérer la deconnexion et mieux gérer les cas limites de reconnexion
# TODO: verifier l'authentification pour les services sensibles
# TODO: injection SQL
# i.e user_data == None




class HTTPHandler(BaseHTTPRequestHandler):
    """HTTPHandler

    This class handles HTTP requests GET, POST, HEAD, OPTIONS
    It manages cookies, sessions, cache and authentication for admin pages

    Attributes:
        sessions: a dictionnary which contains the users' data
    """
    sessions = {}

    def __init__(self, request, client_address, server):
        """ constructor """
        self.actionServlet = action_servlet.ActionServlet()
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

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
        f = self._send_headers()
        if f != None:
            f.close()

    def do_GET(self):
        """ method: GET """
        f = self._send_headers()

        if f != None:
            shutil.copyfileobj(f, self.wfile)
            f.close()

    def _send_headers(self):
        """ define the common headers for HEAD & GET requests """

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
                self.send_response(HTTPStatus.FOUND)
                self.send_header("Location", AUTHENTICATION_PAGE)
                self.end_headers()
                return None

        try:
            f = open(os.curdir + os.sep + path, mode='rb')
        except IOError:
            self.send_error(HTTPStatus.NotFound,'File Not Found: %s' % self.path)
            return None

        # From https://github.com/python/cpython/blob/master/Lib/http/server.py

        try:
            fs = os.fstat(f.fileno())
            # Use browser cache if possible
            if ("If-Modified-Since" in self.headers
                    and "If-None-Match" not in self.headers):
                # compare If-Modified-Since and time of last file modification
                try:
                    ims = email.utils.parsedate_to_datetime(
                        self.headers["If-Modified-Since"])
                except (TypeError, IndexError, OverflowError, ValueError):
                    # ignore ill-formed values
                    pass
                else:
                    if ims.tzinfo is None:
                        # obsolete format with no timezone, cf.
                        # https://tools.ietf.org/html/rfc7231#section-7.1.1.1
                        ims = ims.replace(tzinfo=datetime.timezone.utc)
                    if ims.tzinfo is datetime.timezone.utc:
                        # compare to UTC datetime of last modification
                        last_modif = datetime.datetime.fromtimestamp(
                            fs.st_mtime, datetime.timezone.utc)
                        # remove microseconds, like in If-Modified-Since
                        last_modif = last_modif.replace(microsecond=0)

                        if last_modif <= ims:
                            self.send_response(HTTPStatus.NOT_MODIFIED)
                            if cookies != None:
                                self.send_header('Set-Cookie', cookies.output(header=''))
                            self.end_headers()
                            f.close()
                            return None

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", mimetype)
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            if cookies != None:
                self.send_header('Set-Cookie', cookies.output(header=''))
            self.end_headers()
            return f
        except:
            f.close()
            raise

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
            try:
                user_data, result = self.actionServlet.fetch(user_data, input_data)

                if user_data != None:
                    if "session-id" not in cookies:
                        self._create_session(user_data, cookies)

                    self.sessions[int(cookies["session-id"].value)] = user_data

                self.send_response(HTTPStatus.OK)
                self.send_header('Content-type', "application/javascript")
                self.send_header("Access-Control-Allow-Origin", "*")
                if cookies != None:
                    self.send_header('Set-Cookie', cookies.output(header=''))
                self.end_headers()

                self.wfile.write(result.encode("utf8"))
            except Exception as ex:
                self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal Server Error")
                raise ex


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


