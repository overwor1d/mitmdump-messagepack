from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import msgpack

def hello_world(request):
    packed = msgpack.packb([1, 2, 3], use_bin_type=True)
    return Response(packed)

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

