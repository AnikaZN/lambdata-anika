import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_product_is_string(self):
        prod = Product('Test Product')
        self.assertIsInstance(prod.name, str)

    def test_product_methods(self):
        prod = Product('Test Product')
        theft = prod.stealability()
        boom = prod.explode()
        self.assertIsInstance(theft, tuple)
        self.assertIsInstance(boom, tuple)

#I'm not sure how to keep the defaults while also generating random numbers
#     def test_default_product_price(self):
#         """Test default product price being 10."""
#         prod = Product('Test Product')
#         self.assertEqual(prod.price, 10)



#got stuck here - I think I need to do some studying on testing
# class AcmeReportTests(unittest.TestCase):
#     def test_default_num_products(self):
#         list = generate_products()
#         self.assertIsInstance(list[0], str, str)



if __name__ == '__main__':
    unittest.main()
