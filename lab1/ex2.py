def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


def main():
    input_string = input("Enter a string: ")

    print("The number of vowels in the string is:", count_vowels(input_string))


if __name__ == "__main__":
    main()
