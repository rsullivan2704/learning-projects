# Flask application to connect to wsgi_server.py

from flask import Flask
from flask import Response
flask_app = Flask('flask_app')

@flask_app.route('/hello')
def hello_world():
    # Create flask Response object
    return Response(
        'Hello world from Flask!\n',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app
