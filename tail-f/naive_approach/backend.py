from http.server import HTTPServer, BaseHTTPRequestHandler

current_position = 0

class CustomGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Serve a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:8001')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')

        self.end_headers()
        self.wfile.write(CustomGetHandler.read_file_line_by_line())

    @staticmethod
    def read_file_line_by_line():
        with open("index.log", "rb+") as f:
            global current_position
            f.seek(current_position)
            bytes = f.readline()
            if bytes:
                current_position = f.tell()
            return bytes
            

# Define the IP address and port on which you want to run the server
# Use "0.0.0.0" to make the server accessible from other devices on the network
HOST = "127.0.0.1"
PORT = 8000

# Create an instance of the HTTPServer class with a SimpleHTTPRequestHandler
server = HTTPServer((HOST, PORT), CustomGetHandler)

# Start the server and keep it running until you manually stop it (e.g., by pressing Ctrl+C)
print(f"Serving at http://{HOST}:{PORT}")
server.serve_forever()


# if __name__ == "__main__":

#     CustomGetHandler.read_file_line_by_line()
