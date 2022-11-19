#!/usr/bin/env python3
import http.server
import socketserver
import os
from datetime import datetime
import urlparse

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        parsed = urlparse.urlparse(self.path)

        captured_value = urlparse.parse_qs(parsed.query)['cmd'][0]
        print captured_value
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")
            time = datetime.now().strftime("%H:%M:%S")
            self.wfile.write(str.encode(time))
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
