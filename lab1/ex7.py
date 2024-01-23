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
