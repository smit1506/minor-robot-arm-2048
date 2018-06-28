# define main class of your program in the following fashion
# define what route calls what method of your program
# prefix your route with an unique identifier to prevent conflicts with other programs
# in this sample the identifier is /sample

# Response is an object that can be returned to let the httpserver give a response
from Networking.response import Response
# Enum with preconfigured contentTypes
from Networking.content_types import content_type


class ProgramEntry:
    # do on get
    def do_something(self):
        print('Something')
        response = Response(200)
        response.add_body(content_type['text'], 'Hello world')
        return response

    # do on post
    def do_something_with_data(self, data_type, data):
        print(data_type)
        print(data)
        response = Response(200)
        response.add_body(content_type['text'], 'Hello world')
        return response


# make instance of your class
program = ProgramEntry()

# bind routes to functions
get_routes = {
    '/sample/test': program.do_something
}

post_routes = {
    '/sample/test': program.do_something_with_data
}