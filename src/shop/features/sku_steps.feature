Feature: Managing SKUs

    Scenario: Searching SKUs
        Given I have added a product by SKU
        When I search for the same product by SKU
        Then I receive back an object with the SKU's description, weight per item, count of items, UPC code, and MSRP
