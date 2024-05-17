class Building:

    def __init__(self, buildingType=None):
        self.numberOfFloors = 2
        if buildingType:
            self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


school_1 = Building(buildingType='школа')
school_2 = Building(buildingType='школа')
house_1 = Building(buildingType='дом')
house_2 = Building(buildingType='дом')
print(school_1 == school_2, house_1 == house_2)
print(school_1 == house_1, school_2 == house_2)
print(school_1.numberOfFloors == house_1.numberOfFloors)
print(house_1 != house_2)
