class Bus:
    def __init__(self, trip):
        self.trip = trip

    def navigator (self , stop):
        line = trip[self.trip]
        print(f"Автобус {self.trip} прибыл на остановку {line[stop]}")


trip = {
    13: ("billion", "cdk", "shop", "job"),
    25: ("galaxy_store", "iphone_store", "redmy_store")
}
samsung_galaxy_a54_5g = Bus(13)
for num in range(4):
    samsung_galaxy_a54_5g.navigator(num)
samsung_galaxy_a54 = Bus(25)
for num in range(3):
    samsung_galaxy_a54.navigator(num)
