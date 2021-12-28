# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import location
from http.client import parse_headers
import sys
import json

hostName = "0.0.0.0"
serverPort = 8080

d = location.Database("/var/lib/location/database.db")

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        ip = self.client_address[0]
        #print(parse_headers(self.headers))
        if self.headers.get('X-Forwarded-For') != None:
            ip = self.headers.get('X-Forwarded-For')

        ip = ip.replace(' ', '')
        ip = ip.split(",")

        headers = dict()
        for i in self.headers:
            headers[i] = self.headers.get(i)

        dataSet = {"ip": ip, "header": headers, "country": {}}
        for i in ip:
            n = d.lookup(i)
            if hasattr(n, 'country_code'):
                dataSet['country'][i] = n.country_code

        self.wfile.write(bytes(json.dumps(dataSet), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
