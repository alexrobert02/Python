# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.


def convert_to_lowercase_with_underscores(input_string):
    return input_string.replace(" ", "_").lower()


def main():
    input_string = input("Enter a string in UpperCamelCase: ")

    print("String in lowercase_with_underscores:", convert_to_lowercase_with_underscores(input_string))


if __name__ == "__main__":
    main()
