from BaseHTTPServer import BaseHTTPRequestHandler

from routeDict import get_routes, post_routes
from Networking.response import Response
import re
from Networking.content_types import content_type


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def _set_error_headers(self, code, message=''):
        self.send_error(code, message)
        self.end_headers()

    def handle_response(self, response):
        self.send_response(response.status_code)
        if response.is_error:
            self.send_error(response.status_code, response.message)
        else:
            for header in response.headers.keys():
                self.send_header(header, response.headers[header])
            self.end_headers()
            self.wfile.write(bytes(response.body))
            return
        self.end_headers()

    def parse_path(self, path):
        pathRegex = re.compile('^(.*?)(?:\?|$)')
        return pathRegex.findall(path)[0]


    def do_GET(self):
        path = self.parse_path(self.path)
        if path in get_routes.keys():
            response = get_routes[path]()
            if isinstance(response, Response):
                self.handle_response(response)
                return
            self._set_headers()
        self._set_headers()



    def do_POST(self):
        path = self.parse_path(self.path)
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        content_type = self.headers['Content-type']
        if path in post_routes.keys():
            response = post_routes[path](content_type, content)
            if isinstance(response, Response):
                self.handle_response(response)
                return
        self._set_headers()

