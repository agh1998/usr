#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
from user import Action
import json


# HTTPRequestHandler class
class userHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        print()
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        #interact with db
        # /favorite?username=<username> fetch all favorites of user
        # /history?username=<username> fetch all history of user
        # /favorite?username=<username>&id=<id> add id to user's favorites
        # /history?username=<username>&id=<id> add id to user's history
        # /reset reset database

        action = self.pathParcing(self.path)
        result = Action(action).act()

        # Send message back to client
        message = json.dumps(result)
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def pathParcing(self,path):
        if path == '/reset':
            return ['reset',None,None]
        args = []
        type, paras = path[1:].split('?')
        args.append(type)
        if '&' in paras:
            usr, id = paras.split('&')
            args.extend([usr.split('=')[1], id.split('=')[1]])
        else:
            args.append(paras.split('=')[1])
            args.append(None)
        return args



def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, userHandler)
    print('running server...')
    httpd.serve_forever()


run()
