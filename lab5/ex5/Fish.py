from Animal import Animal


class Fish(Animal):
    def __init__(self, species, habitat, scale_color):
        super().__init__(species, habitat)
        self.scale_color = scale_color

    def display_info(self):
        super().display_info()
        print(f"Scale color: {self.scale_color}")

    def lay_eggs(self):
        print(f"{self.species} is laying eggs in water.")

    def move(self):
        print(f"{self.species} swims in the water.")
