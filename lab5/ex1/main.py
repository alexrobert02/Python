from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle


def main():
    circle = Circle(6)
    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())

    rectangle = Rectangle(5, 7)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())

    triangle = Triangle(3, 4, 5)
    print("Triangle area:", triangle.area())
    print("Triangle perimeter:", triangle.perimeter())


if __name__ == '__main__':
    main()
