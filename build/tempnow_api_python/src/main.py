
import os
# IMPORTS MEUS
from common.util import CustomJSONEncoder
# IMPORTS FLASK
from flask.helpers import locked_cached_property
from flask import Flask
from flask_cors import CORS

class MyConfig(object):
    RESTFUL_JSON = {
        'cls': CustomJSONEncoder
    } # add whatever settings here

    @staticmethod
    def init_app(app):
        app.config['RESTFUL_JSON']['cls'] = app.json_encoder = CustomJSONEncoder
        app.config['PROFILE'] = False

app = Flask(__name__)
app.config.from_object(MyConfig)
MyConfig.init_app(app)
CORS(app)

from routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    #from werkzeug.contrib.profiler import ProfilerMiddleware
    #app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[50])
    port = os.getenv('PORT', '8000')  # pylint: disable=C0103
    host = os.getenv('HOST', '0.0.0.0')  # pylint: disable=C0103
    debug = os.getenv('DEBUG', 'FALSE') == 'TRUE'  # pylint: disable=C0103

    app.run(host=host, port=int(port), debug=debug)


