class ProductValidator:
    def validate(self, product):
        if 'description' in product and product['description'] == '':
            return ["Product does not have text in it's description field"]
        return ["Product does not have a description field"]
