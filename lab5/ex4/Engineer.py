#   Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like
# Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their
# roles.


from Employee import Employee


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code.")
