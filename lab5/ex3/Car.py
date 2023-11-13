from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.mileage = None

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

    def calculate_mileage(self, kilometers_driven, fuel_used):
        self.mileage = kilometers_driven / fuel_used
