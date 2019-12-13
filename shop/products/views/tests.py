from unittest import TestCase
from unittest.mock import MagicMock

from .add_products import AddProductsView
from ..services.product_validator import ProductValidator


class FakeRequest:
    pass


PRODUCT_JSON = '''{
            "description": "Something",
            "unit_weight": "14.4 oz",
            "count": 250,
            "upc": "78087204980",
            "msrp": "$7.00"
        }'''.strip('\n\r')


class AddProductsViewTests(TestCase):
    def setUp(self):
        view = AddProductsView()
        view.validator = MagicMock(spec_set=ProductValidator())
        view.validator.validate.return_value = []

        fake_request = FakeRequest()
        fake_request.body = PRODUCT_JSON

        self.view = view
        self.fake_request = fake_request

    def test_should_have_response_status_code_of_201(self):
        response = self.view.post(self.fake_request)

        self.assertEqual(response.status_code, 201)

    def test_should_have_response_content_type_of_application_json(self):
        response = self.view.post(self.fake_request)

        self.assertEqual(response.get('content-type'), 'application/json')

    def test_should_have_response_status_code_of_400_if_product_is_invalid(self):
        self.view.validator.validate.return_value = ['this', 'is', 'an', 'error']

        response = self.view.post(self.fake_request)

        self.assertEqual(response.status_code, 400)
