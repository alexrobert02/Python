from Mammal import Mammal
from Bird import Bird
from Fish import Fish


def main():
    racoon = Mammal("Racoon", "Grasslands", "Yellow")
    sparrow = Bird("Parrot", "Tropical forests", "Red")
    shark = Fish("Shark", "Oceans", "Gray")

    racoon.display_info()
    print("\n")

    sparrow.display_info()
    print("\n")

    shark.display_info()
    print("\n")

    racoon.give_birth()
    sparrow.lay_eggs()
    shark.lay_eggs()
    print("\n")

    racoon.move()
    sparrow.move()
    shark.move()


if __name__ == '__main__':
    main()
