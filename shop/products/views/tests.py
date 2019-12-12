from django.test import TestCase

from .add_products import AddProductsView


class AddProductsViewTests(TestCase):
    def test_should_have_response_status_code_of_201(self):
        view = AddProductsView()
        res = view.post({})

        assert res.status_code == 201

    def test_should_have_response_content_type_of_application_json(self):
        view = AddProductsView()
        res = view.post({})

        assert res.get('Content-Type') == 'application/json'
