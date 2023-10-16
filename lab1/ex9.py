#   Write a functions that determine the most common letter in a string. For example if the string is "an apple is not
# a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing
# should not be considered "A" and "a" represent the same character.


def most_common_letter(string):
    letter_count = {}
    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    most_common = max(letter_count, key=letter_count.get)
    most_common_count = letter_count[most_common]

    return most_common, most_common_count


def main():
    input_string = "an apple is not a tomato"
    common_letter, count = most_common_letter(input_string)

    print(f"The most common letter is '{common_letter}' with a count of {count}.")


if __name__ == "__main__":
    main()
