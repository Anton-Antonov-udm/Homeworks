class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        self.name = 'building_' + str(Building.total)


buildings = []
while len(buildings) < 40:
    building = Building()
    buildings.append(building.name)

print(Building.total)
print(buildings)
