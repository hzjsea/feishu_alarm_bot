from http.server import BaseHTTPRequestHandler, HTTPServer
from bot import RequestHandler


def run():
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print("start.....")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
