from Animal import Animal


class Bird(Animal):
    def __init__(self, species, habitat, feather_color):
        super().__init__(species, habitat)
        self.feather_color = feather_color

    def display_info(self):
        super().display_info()
        print(f"Feather color: {self.feather_color}")

    def lay_eggs(self):
        print(f"{self.species} is laying eggs.")

    def move(self):
        print(f"{self.species} flies in the sky.")
