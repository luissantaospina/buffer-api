from flask import Flask
from config import Config
from flask_cors import CORS
from .routes import api_routes


app = Flask(__name__)
app.config.from_object(Config)
app_context = app.app_context()
app_context.push()
cors = CORS(app)

app.register_blueprint(api_routes, url_prefix='/api/v1')
