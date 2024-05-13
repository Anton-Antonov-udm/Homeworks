class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Вы находитесь на {floors} этаже')


house = House()
house.setNewNumberOfFloors(11)
print(f'Вы находитесь на {house.numberOfFloors} этаже')
