from django.test import TestCase

from .product import Product


class ProductTest(TestCase):
    def test_from_json_converts_all_fields(self):
        json_dictionary = {
            'description': '11 oz Beverage Mug',
            'unit_weight': '14.4 oz',
            'count': 250,
            'upc': '78087204980',
            'msrp': '$7.00',
        }

        product = Product.from_json(json_dictionary)
        self.assertEqual(json_dictionary['description'], product.description)
        self.assertEqual(json_dictionary['unit_weight'], product.unit_weight)
        self.assertEqual(json_dictionary['count'], product.count)
        self.assertEqual(json_dictionary['upc'], product.upc)
        self.assertEqual(json_dictionary['msrp'], product.msrp)

    def test_from_json_raises_key_error_if_an_expected_key_is_not_found(self):
        self.assertRaises(KeyError, Product.from_json, {})

    def test_from_json_raises_type_error_if_non_dictionary_is_passed(self):
        self.assertRaises(TypeError, Product.from_json, '')
