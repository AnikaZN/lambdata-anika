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

    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        list = generate_products()
        self.assertEqual(len(list), 30)

    def test_legal_names(self):
        list = generate_products()
        for x in list:
            name = x[0]
        self.assertIs(type(name), tuple)
        self.assertIn(name[0], ADJECTIVES)
        self.assertIn(name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
