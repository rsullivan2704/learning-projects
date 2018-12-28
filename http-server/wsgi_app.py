def app(environ, start_response):
    """A barebones WSGI application.

    This is a starting point for a custom Web Framework
    """

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    # Invoke the start_response callable
    start_response(status, response_headers)
    # Build the response body and return it
    return ['Hello world from a simple WSGI application!\n'.encode('utf-8')]
