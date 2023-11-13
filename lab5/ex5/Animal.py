class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def display_info(self):
        print(f"species: {self.species}")
        print(f"Habitat: {self.habitat}")

    def move(self):
        pass
