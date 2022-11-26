#!/usr/bin/env python3
import http.server
import socketserver
import os
from datetime import datetime
from urllib import parse
import json


class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)

        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=UTF-8")
        self.end_headers()  

        try:
            string = parse.parse_qs(parse.urlparse(self.path).query)['str'][0]
        except:
            string = ''

        letters = [*string]

        lowercase = len([letter for letter in letters if letter.islower()])
        uppercase = len([letter for letter in letters if letter.isupper()])
        digits = len([letter for letter in letters if letter.isdigit()])
        special = len(letters) - (lowercase + uppercase + digits)

        response = { "lowercase" : lowercase, "uppercase" : uppercase, "digits" : digits, "special" : special}

        self.wfile.write(str.encode(json.dumps(response)))

    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
