from unittest import TestCase

from .product_validator import ProductValidator


class ProductValidatorTests(TestCase):
    def test_should_fail_if_product_has_no_description_field(self):
        product = {
            'unit_weight': '14.4 oz',
            'count': 250,
            'upc': '78087204980',
            'msrp': '$7.00',
        }
        validator = ProductValidator()
        errors = validator.validate(product)

        assert "Product does not have a description field" in errors

    def test_should_fail_if_product_has_no_description_text(self):
        product = {
            'description': '',
            'unit_weight': '14.4 oz',
            'count': 250,
            'upc': '78087204980',
            'msrp': '$7.00',
        }

        validator = ProductValidator()
        errors = validator.validate(product)

        assert len(errors) == 1
        assert "Product does not have text in it's description field" in errors
