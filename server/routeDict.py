from App.program_entry import get_routes as get_routes1, post_routes as post_routes1
from Networking.response import Response

def some_day():
    print('I like trains')

    return Response(status_code=200, message="train")


def some_day_with_data(data_type, data):
    print(data_type)
    print(data)


get_routes = {
    '/test': some_day
}

get_routes.update(get_routes1)

post_routes = {
    '/hola': some_day_with_data
}

post_routes.update(post_routes1)
