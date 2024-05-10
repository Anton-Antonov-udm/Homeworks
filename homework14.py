class House:

    def __init__(self):
        self.number = 1


house = House()
house.numberOfFloors = 10
floor = 1
while house.numberOfFloors >= floor:
    print('Текущий этаж равен', floor)
    floor += 1
