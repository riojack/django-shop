import simplejson
from django.http import HttpResponse
from django.views import View


class SearchProductsView(View):
    def post(self, request):
        ish = simplejson.dumps([{
            'description': '11 oz Beverage Mug',
            'unit_weight': '14.4 oz',
            'count': 250,
            'upc': '78087204980',
            'msrp': '$7.00',
        }])
        return HttpResponse(ish, content_type='application/json', status=200)
