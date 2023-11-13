from Book import Book
from DVD import DVD
from Magazine import Magazine


def main():
    book = Book("Moby Dick", "Moby Dick", "B001", "Adventure fiction")
    dvd = DVD("Inception", "Christopher Nolan", "D001", "2 hours 28 minutes")
    magazine = Magazine("Healthy Food", "Healthy Food Society", "M001", 123)

    print("Magazine information:")
    book.display_info()
    print()
    book.check_out()
    book.display_info()
    print("\n")
    book.return_item()
    book.display_info()
    print("\n")

    print("DVD information:")
    dvd.display_info()
    print("\n")
    dvd.check_out()
    dvd.display_info()
    print("\n")

    print("Magazine information:")
    magazine.display_info()
    print("\n")
    magazine.check_out()
    magazine.display_info()


if __name__ == '__main__':
    main()
