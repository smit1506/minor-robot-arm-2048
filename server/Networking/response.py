from content_types import content_type

class Response:
    def __init__(self, status_code, message=''):
        self.status_code = status_code
        self.message = message
        self.headers = {}
        self.body = ''
        self.is_error = not(200 <= status_code < 300)
        if not self.is_error:
            self.headers['Content-type'] = content_type['text']
            self.body = self.message

    def add_header(self, header_name, header_value):
        self.headers[header_name] = header_value

    def add_body(self, body_type, body):
        self.headers['Content-type'] = body_type
        self.body = body
