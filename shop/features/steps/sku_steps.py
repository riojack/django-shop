import requests
from behave import use_step_matcher, given, when, then

use_step_matcher("re")


@given("I have added a product by SKU")
def step_i_have_added_a_product_by_sku(context):
    sku = {
        'description': '11 oz Beverage Mug',
        'unit_weight': '14.4 oz',
        'count': 250,
        'upc': '78087204980',
        'msrp': '$7.00',
    }
    req = requests.post(context.get_url('/products/'), json=sku, allow_redirects=False)
    assert req.status_code == requests.codes.created


@when("I search for the same product by SKU")
def step_i_search_for_the_same_product_by_sku(context):
    search_parameters = {
        'sku_name': '11 oz Beverage Mug'
    }
    req = requests.post(context.get_url('/products/search'), json=search_parameters, allow_redirects=False)
    assert req.status_code == requests.codes.ok
    context.search_results = req.json()


@then("I receive back an object with the SKU's description, weight per item, count of items, UPC code, and MSRP")
def step_i_receive_back_an_object_with_the_skus_description_weight_per_item_count_of_items_upc_code_and_msrp(context):
    expected_sku = {
        'description': '11 oz Beverage Mug',
        'unit_weight': '14.4 oz',
        'count': 250,
        'upc': '78087204980',
        'msrp': '$7.00',
    }
    assert len(context.search_results) == 1
    assert context.search_results[0] == expected_sku
