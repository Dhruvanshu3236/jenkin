from Product.models import Product


class ProductService:
    def get_product():
        products = [
            {'id':'1', 'name':'Apple'},
            {'id':'2', 'name':'Banana'},
        ] 
        return products

