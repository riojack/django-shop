## Shop
A generic RESTful service for buying products from a shop.

### Acceptance Criteria
The API must meet these criteria.  The user ("I" below) is another system such as a front-end or service.

```gherkin
Given I have added a product by SKU
When I search for the same product by SKU
Then I receive back an object with the SKU's description, weight per item, count of items, UPC code, and MSRP
```
