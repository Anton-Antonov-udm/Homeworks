# - Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#
# - Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошадиных сил для автомобиля
#
# - Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
#
# - Создайте экземпляр класса Nissan и распечатайте через функцию print vehicle_type, price


class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1_000_000

    def horse_powers(self, power):
        res = f'У машины {power} лошадиных сил'
        print(res)
        return res


class Nissan(Vehicle, Car):
    vehicle_type = 'внедорожник'
    price = 1_500_000

    def horse_powers(self, power):
        super().horse_powers(power)
        print(f'Это {self.vehicle_type}. У него {power} лошадиных сил')


nissan = Nissan()
nissan.horse_powers(150)
print(nissan.vehicle_type)
print(nissan.price)