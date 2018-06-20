from http.server import BaseHTTPRequestHandler, HTTPServer


class testHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()
#open("../html/lksh/main.html", "r")
        message = "HI WORLD!"
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer)
    print('running server...')
    httpd.serve_forever()


run()
