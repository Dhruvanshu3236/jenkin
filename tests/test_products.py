import pytest
from flask import url_for
from src.app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['SERVER_NAME'] = 'localhost:5000'
    return app

@pytest.fixture()
def client(app):
    app.app_context().push()
    with app.test_client() as client:
        yield client

def test_product_api(client):
    res = client.get(url_for('product_api.get_product'))
    res.json == 2011
