from flask import Flask
from Product.api import product_api


def create_app(config=None):

    app = Flask(__name__)

    ## register blueprint
    app.register_blueprint(product_api)

    return app