import json

from django.http import HttpResponse
from django.views import View


class AddProductsView(View):
    validator = None

    def post(self, request):
        product = json.loads(request.body)
        status_code = 201
        if len(self.validator.validate(product)) > 0:
            status_code = 400
        return HttpResponse('', content_type='application/json', status=status_code)
