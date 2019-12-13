from unittest import TestCase
from unittest.mock import patch, PropertyMock

from .add_products import AddProductsView


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
        self.fakeHttpRequestClassPatcher = patch('django.http.HttpRequest', spec=True)
        self.fakeProductValidatorClassPatcher = patch('products.services.product_validator.ProductValidator', spec=True)

        FakeHttpRequestClass = self.fakeHttpRequestClassPatcher.start()
        FakeProductValidatorClass = self.fakeProductValidatorClassPatcher.start()

        view = AddProductsView()
        view.validator = FakeProductValidatorClass()
        view.validator.validate.return_value = []

        fake_request = FakeHttpRequestClass()
        type(fake_request).body = PropertyMock(return_value=PRODUCT_JSON)
        # For an explanation of the grossness above, see...
        # https://docs.python.org/3.7/library/unittest.mock.html#unittest.mock.PropertyMock

        self.view = view
        self.fake_request = fake_request

    def tearDown(self):
        self.fakeHttpRequestClassPatcher.stop()
        self.fakeProductValidatorClassPatcher.stop()

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
