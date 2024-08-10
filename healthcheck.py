from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


def run(server_class=HTTPServer, handler_class=HealthCheck, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting health check server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

