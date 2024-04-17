from flask import jsonify, Blueprint
from Product.models import Product
from Product.services import ProductService

product_api = Blueprint('product_api', __name__)

@product_api.route('/products', methods=['GET'])
def get_product():
    products = ProductService.get_product()
    data = Product(many=True).dump(products)
    return jsonify(data), 200

