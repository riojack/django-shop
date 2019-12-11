import simplejson
from django.http import HttpResponse


def add_product(request):
    return HttpResponse('', status=201)


def search_products(request):
    ish = simplejson.dumps([{
        'description': '11 oz Beverage Mug',
        'unit_weight': '14.4 oz',
        'count': 250,
        'upc': '78087204980',
        'msrp': '$7.00',
    }])
    return HttpResponse(ish, content_type='application/json', status=200)
