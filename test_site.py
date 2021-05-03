import http.server
import threading
import socketserver
from test_globals import PORT, SITE_LOCATION

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = SITE_LOCATION
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        pass


class TestServer():

    def __init__(self):
        handler_object = MyHttpRequestHandler
        self.server = socketserver.TCPServer(("", PORT), handler_object)

    def start_server(self):
        threading.Thread(target=self.server.serve_forever).start()

    def stop_server(self):
        self.server.shutdown()


server = TestServer()
server.start_server()