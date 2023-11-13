from Employee import Employee


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Sales Target: ${self.sales_target}")

    def make_sale(self):
        print(f"{self.name} makes a sale of ${self.sales_target}.")
