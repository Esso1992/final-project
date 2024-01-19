# features/products.feature

Feature: Product Management

  Background:
    Given the following products exist
      | name         | category     | availability |
      | ProductA     | Electronics  | In Stock      |
      | ProductB     | Clothing     | Out of Stock  |
      | ProductC     | Furniture    | In Stock      |
      # Add more products as needed

  Scenario: Read product details
    When I request the details for "ProductA"
    Then I should see the details for "ProductA" including:
      | category     | Electronics  |
      | availability | In Stock      |

  Scenario: Update product details
    When I update the details for "ProductB" to:
      | category     | Accessories  |
      | availability | In Stock      |
    Then I should see the updated details for "ProductB" including:
      | category     | Accessories  |
      | availability | In Stock      |

  Scenario: Delete a product
    When I delete the product "ProductC"
    Then the product "ProductC" should not exist

  Scenario: List all products
    When I request the list of all products
    Then I should see the following products:
      | name         | category     | availability |
      | ProductA     | Electronics  | In Stock      |
      | ProductB     | Accessories  | In Stock      |

  Scenario: Search products by name
    When I search for products with the name "ProductA"
    Then I should see the following products:
      | name         | category     | availability |
      | ProductA     | Electronics  | In Stock      |

  Scenario: Search products by category
    When I search for products in the category "Clothing"
    Then I should see the following products:
      | name         | category     | availability |
      | ProductB     | Accessories  | In Stock      |

  Scenario: Search products by availability
    When I search for products with availability "Out of Stock"
    Then I should see the following products:
      | name         | category     | availability |
      | ProductB     | Accessories  | Out of Stock  |

