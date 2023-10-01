from http.server import BaseHTTPRequestHandler, HTTPServer


class CustomFrontEndServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Serve a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.read_html_file())

    def read_html_file(self):
        with open(f"index.html", "rb") as f:
            return f.read()


HOST, PORT = "127.0.0.1", 8001

server = HTTPServer((HOST, PORT), CustomFrontEndServer)

print(f"Fronted Serving at http://{HOST}:{PORT}")
server.serve_forever()
