class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def distance(self, other_location: list) -> float:
        return ((self.location[0] - other_location[0]) ** 2
                + (self.location[1] - other_location[1]) ** 2) ** 0.5
