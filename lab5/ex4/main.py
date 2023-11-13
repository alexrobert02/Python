from Manager import Manager
from Engineer import Engineer
from Salesperson import Salesperson


def main():
    manager = Manager("Anderson Milo", "M001", 80000, 10)
    engineer = Engineer("Stan Tucker", "E001", 60000, "Python")
    salesperson = Salesperson("Ivan Teresa", "S001", 70000, 100000)

    print("Manager information:")
    manager.display_info()
    manager.conduct_meeting()

    print("\nEngineer information:")
    engineer.display_info()
    engineer.write_code()

    print("\nSalesperson information:")
    salesperson.display_info()
    salesperson.make_sale()


if __name__ == '__main__':
    main()
