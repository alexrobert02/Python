from Animal import Animal


class Mammal(Animal):
    def __init__(self, species, habitat, fur_color):
        super().__init__(species, habitat)
        self.fur_color = fur_color

    def display_info(self):
        super().display_info()
        print(f"Fur color: {self.fur_color}")

    def give_birth(self):
        print(f"{self.species} is giving birth to live young.")

    def move(self):
        print(f"{self.species} walks on four legs.")
