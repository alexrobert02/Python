#   Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the
# first number that is found.


def extract_number_from_text(text):
    number_found = False
    number_string = ""

    for char in text:
        if char.isdigit():
            number_string += char
            number_found = True
        elif number_found:
            break

    return int(number_string)


def main():
    text1 = "An apple is 123 USD"
    text2 = "abc123abc"

    print("Result 1:", extract_number_from_text(text1))
    print("Result 2:", extract_number_from_text(text2))


if __name__ == "__main__":
    main()
