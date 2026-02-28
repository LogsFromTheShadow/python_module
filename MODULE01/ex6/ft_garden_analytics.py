class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def display_status(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Demonstrates inheritance:
    Inherits attributes and methods from the Plant base class.
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.isblooming: bool = True

    def display_status(self) -> str:
        status = "blooming" if self.isblooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    """
    Demonstrates multi-level inheritance:
    Inherits from FloweringPlant, which inherits from Plant.
    """

    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def display_status(self) -> str:
        status = "blooming" if self.isblooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"({status}), Prize points: {self.points}")


class GardenManager:
    """
    Main manager class demonstrating composition (holding Plant objects)
    and class-level attributes.
    """
    gardener: int = 0

    class GardenStats:
        """
        Nested class (Inner class):
        Acts as a helper component specifically for GardenManager statistics.
        """

        def __init__(self, plants: list[Plant]) -> None:
            self.plants = plants

        def get_types(self) -> tuple[int, int, int]:
            reg = sum(1 for p in self.plants if type(p) is Plant)
            flow = sum(1 for p in self.plants if type(p) is FloweringPlant)
            prize = sum(1 for p in self.plants if type(p) is PrizeFlower)
            return reg, flow, prize

        def get_score(self) -> int:
            score = 0
            for p in self.plants:
                score += p.height
                if isinstance(p, FloweringPlant):
                    score += 15
                if isinstance(p, PrizeFlower):
                    score += p.points
            return score

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []
        GardenManager.gardener += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def garden_report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.display_status()}")

        stats = self.GardenStats(self.plants)
        reg, flow, prize = stats.get_types()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {len(self.plants)}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")

    def get_score(self) -> int:
        return self.GardenStats(self.plants).get_score()

    @classmethod
    def create_garden_network(cls, names: list[str]) -> list['GardenManager']:
        """
        Class method:
        Operates on the class itself (cls) rather than an instance.
        Often used as an alternative constructor.
        """
        return [cls(name) for name in names]

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Static method:
        A utility function that belongs to the class namespace but doesn't
        need access to class (cls) or instance (self) data.
        """
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()
    alice.garden_report()

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob = GardenManager("Bob")
    bob.plants.extend([Plant("Pine", 40), FloweringPlant("Tulip", 37, "pink")])

    print(f"Garden scores - Alice: {alice.get_score()},"
          f" Bob: {bob.get_score()}")
    print(f"Total gardens managed: {GardenManager.gardener}")
