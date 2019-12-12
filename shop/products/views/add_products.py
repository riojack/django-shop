import json

from django.http import HttpResponse
from django.views import View

from ..services.product_validator import ProductValidator


class AddProductsView(View):
    def post(self, request):
        validator = ProductValidator()
        product = json.loads(request.body)
        status_code = 201
        if len(validator.validate(product)) > 0:
            status_code = 400
        return HttpResponse('', content_type='application/json', status=status_code)
