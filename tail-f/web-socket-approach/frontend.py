from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8001

class CustomHttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.read_html_file())   
    
    def read_html_file(self):
        with open(f"index.html", "rb") as f:
            return f.read()
        

server = HTTPServer((HOST, PORT), CustomHttpHandler)
print(f"Serving at http://{HOST}:{PORT}")
server.serve_forever()