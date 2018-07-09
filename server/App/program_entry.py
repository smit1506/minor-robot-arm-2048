# define main class of your program in the following fashion
# define what route calls what method of your program
# prefix your route with an unique identifier to prevent conflicts with other programs
# in this sample the identifier is /sample

# Response is an object that can be returned to let the httpserver give a response
from Networking.response import Response
# Enum with preconfigured contentTypes
from Networking.content_types import content_type

import json

from App import main

class ProgramEntry:
    
    def calibrate(self, data_type, data):
        response = Response(200)
        main.calibrate(data)
        response.add_body(content_type['text'], '1')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def init(self):
        print('Initializing...')
        response = Response(200)
        value = '0'
        if main.init():
            print "Found field, returning 1"
            value = '1'
        response.add_body(content_type['text'], value)
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def fetch_image(self):
        print('Fetching image')
        response = Response(200)
        main.getCameraImage()
        response.add_body(content_type['text'], '1')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def auto_move(self):
        print('Running program')
        response = Response(200)
        data = main.run()
        response.add_body(content_type['json'], json.dumps(data))
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def move(self, data_type, data):
        response = Response(200)
        if (data == 'start'):
            main.goToStart()
        response.add_body(content_type['text'], '1')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def set_field(self, data_type, data):
        response = Response(200)
        value = '0'
        if main.setFieldTemplate(map(int, data.split(","))):
            value = '1'
        response.add_body(content_type['text'], value)
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

# make instance of your class
program = ProgramEntry()

# bind routes to functions
get_routes = {
    '/sample/test': program.do_something,
    '/init': program.init,
    '/run': program.auto_move,
    '/image': program.fetch_image
}

post_routes = {
    '/sample/test': program.do_something_with_data,
    '/field': program.set_field,
    '/calibrate': program.calibrate,
    '/move': program.move
}
