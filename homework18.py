class Car:
    name = 'Машина'
    price = 1000000

    def __str__(self):
        return '{} стоит {} и имеет под капотом {} лошадиных сил'.format(
            self.name, self.price, self.horse_powers())

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return 150


class Kia(Car):
    name = 'Киа'
    price = 2000000

    def horse_powers(self):
        return 200


car = Car()
print(car)

nissan = Nissan()
nissan.name = 'Ниссан'
print(nissan)

kia = Kia()
print(kia)
kia.price = 1750000
print(kia)
