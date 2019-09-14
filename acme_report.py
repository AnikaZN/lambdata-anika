import random
from acme import Product, BoxingGlove

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=5):  #changed to 5 for testing purposes
    products = []
    while n > 0:
        x = (random.choice(ADJECTIVES), random.choice(NOUNS))
        products.append(x)
        n = n-1

#I was having a hard time figuring out the inventory report so I went with
#something a little different
    for p in products:
        example = Product(p)
        report = example.summary()


if __name__ == '__main__':
    generate_products()
