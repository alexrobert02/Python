def most_common_letter(string):
    letter_count = {}
    for char in string:
        if char != ' ':
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count


def main():
    print(most_common_letter("Ana has apples."))


if __name__ == '__main__':
    main()
