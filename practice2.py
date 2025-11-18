class Spacecraft:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Shuttle(Spacecraft):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}, Model: {self.model}")
        print(f"Number of engines: {self.engine}")