from Employee import Employee


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a team meeting.")
