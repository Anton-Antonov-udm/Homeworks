import time
from threading import Thread
from time import sleep


class Knight(Thread):
    enemies = 100

    def __init__(self, name, power):
        self.knight_name = name
        self.POWER = power
        super().__init__()

    def run(self):
        hits = self.enemies // self.POWER
        print(f'{self.knight_name}, на нас напали!')
        for i in range(hits):
            self.enemies -= self.POWER
            print(f'{self.knight_name} сражается {i + 1}..., осталось {self.enemies} воинов.')
            time.sleep(1)
        print(f'{self.knight_name} одержал победу спустя {hits} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
