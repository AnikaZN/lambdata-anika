import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    n = num_products
    while n > 0:
        name = (random.choice(ADJECTIVES), random.choice(NOUNS))
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0, 2.5)
        product = (name, price, weight, flammability)
        products.append(product)
        n = n-1
    return products


def inventory_report(products):
    prices = []
    weights = []
    flammabilities = []
    for x in products:
        price = x[1]
        prices.append(price)
        mean_prices = (sum(prices)/len(prices))

        weight = x[2]
        weights.append(weight)
        mean_weights = (sum(weights)/len(weights))

        flammability = x[3]
        flammabilities.append(flammability)
        mean_flammabilities = (sum(flammabilities)/len(flammabilities))

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Product Count:', len(products))
    print('Average Price:', round(mean_prices))
    print('Average Weight:', round(mean_weights))
    print('Average Flammability:', round(mean_flammabilities))


if __name__ == '__main__':
    inventory_report(generate_products())
