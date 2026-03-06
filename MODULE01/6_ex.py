class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        return f"{self.name} grew 1cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.isblooming = True


class PrizeFlower(Plant):
    def __init__(self, name, height, color, prizepoints):
        super().__init__(name, height, color)
        self.prizepoints = prizepoints


class GardenManager:
    Gardener = 0

    class GardenStats:
        def __init__(self, plant):
            self.plant = plant

    def __init__(self, name):
        self.name = name
        self.plants = []


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    Oak = Plant("Oak", 101)
    Rose = FloweringPlant("Rose", 26, "red")
    Sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    
    
