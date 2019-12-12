from django.http import HttpResponse
from django.views import View


class AddProductsView(View):
    def post(self, request):
        return HttpResponse('', content_type='application/json', status=201)
