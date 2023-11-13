from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def display_info(self):
        super().display_info()
        print(f"Towing capacity: {self.towing_capacity}kg")

    def calculate_towing_capacity(self, payload_weight):
        return self.towing_capacity - payload_weight
