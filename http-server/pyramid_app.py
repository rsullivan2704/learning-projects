# Pyramid application to connect to wsgi_server.py

from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    # Create the pyramid response object
    return Response(
        'Hello world from Pyramid!\n',
        content_type='text/plain',
    )

# Add configuration
config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()
