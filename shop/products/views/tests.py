from unittest import TestCase
from unittest.mock import MagicMock

from .add_products import AddProductsView
from ..services.product_validator import ProductValidator


class FakeRequest:
    pass


VALID_PRODUCT = '''{
            "description": "Something",
            "unit_weight": "14.4 oz",
            "count": 250,
            "upc": "78087204980",
            "msrp": "$7.00"
        }'''.strip('\n\r')

INVALID_PRODUCT = '''{
            "description": "",
            "unit_weight": "14.4 oz",
            "count": 250,
            "upc": "78087204980",
            "msrp": "$7.00"
        }'''.strip('\n\r')


class AddProductsViewTests(TestCase):
    def test_should_have_response_status_code_of_201(self):
        view = AddProductsView()
        view.validator = MagicMock(spec_set=ProductValidator())
        view.validator.validate.return_value = []
        fake_req = FakeRequest()
        fake_req.body = VALID_PRODUCT

        res = view.post(fake_req)

        self.assertEqual(res.status_code, 201)

    def test_should_have_response_content_type_of_application_json(self):
        view = AddProductsView()
        view.validator = MagicMock(spec_set=ProductValidator())
        view.validator.validate.return_value = []
        fake_req = FakeRequest()
        fake_req.body = VALID_PRODUCT

        res = view.post(fake_req)

        self.assertEqual(res.get('content-type'), 'application/json')

    def test_should_have_response_status_code_of_400_if_product_is_invalid(self):
        view = AddProductsView()
        view.validator = MagicMock(spec_set=ProductValidator())
        view.validator.validate.return_value = ['this', 'is', 'an', 'error']
        fake_req = FakeRequest()
        fake_req.body = INVALID_PRODUCT

        res = view.post(fake_req)

        self.assertEqual(res.status_code, 400)
