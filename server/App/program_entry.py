# define main class of your program in the following fashion
# define what route calls what method of your program
# prefix your route with an unique identifier to prevent conflicts with other programs
# in this sample the identifier is /sample

# Response is an object that can be returned to let the httpserver give a response
from Networking.response import Response
# Enum with preconfigured contentTypes
from Networking.content_types import content_type

from App import main

class ProgramEntry:
    # do on get
    def do_something(self):
        print('Something')
        response = Response(200)
        #response.add_header('Access-Control-Allow-Origin','*')
        response.add_body(content_type['text'], 'Hello world')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    # do on post
    def do_something_with_data(self, data_type, data):
        print(data_type)
        print(data)
        response = Response(200)
        response.add_body(content_type['text'], 'Hello world')
        return response

    def init(self):
        print('Initializing...')
        response = Response(200)
        #response.add_header('Access-Control-Allow-Origin','*')
        main.init()
        response.add_body(content_type['text'], '1')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response

    def run_program(self):
        print('Running program')
        response = Response(200)
        #response.add_header('Access-Control-Allow-Origin','*')
        main.run()
        response.add_body(content_type['text'], '1')
        response.add_header("Access-Control-Allow-Origin", "http://localhost:8000")
        return response


# make instance of your class
program = ProgramEntry()

# bind routes to functions
get_routes = {
    '/sample/test': program.do_something,
    '/init': program.init,
    '/run': program.run_program
}

post_routes = {
    '/sample/test': program.do_something_with_data
}
