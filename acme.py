import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=1):
        self.name = name
        self.price = random.randint(5, 101)
        self.weight = random.randint(5, 101)
        self.flammability = random.uniform(0.0, 2.5)
        self.identifier = random.randint(1000000, 100000000)

    def stealability(self):
        value = self.price / self.weight
        if value < 0.5:
            return (round(value), 'Not so stealable...')
        elif value >= 0.5 and value < 1.0:
            return (round(value), 'Kinda stealable')
        else:
            return (round(value), 'Very stealable!')

    def explode(self):
        danger = self.flammability * self.weight
        if danger < 10:
            return (round(danger), '...fizzle')
        elif danger >= 10 and danger < 50:
            return (round(danger), '...boom!')
        else:
            return (round(danger), '...BABOOM!!')

    def summary(self):
        sample = Product('Toy')
        print('ACME CORPORATION PRODUCT SUMMARY')
        print('Product:', self.name)
        print('Stealability:', sample.stealability())
        print('Explosion Type', sample.explode())


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=1):
        super().__init__(name, price, flammability, identifier)
        self.weight = weight

    def explode(self):
        return ("...it's a glove")

    def punch(self):
        if self.weight < 5:
            return ('That tickles.')
        elif self.weight >= 5 and self.weight < 15:
            return ('Hey, that hurt!')
        else:
            return ('OUCH!!')
