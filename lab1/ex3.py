def count_occurrences(substring, string):
    count = 0
    index = 0

    while index is not None:
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count


def main():
    substring = input("Enter the first string: ")
    string = input("Enter the second string: ")

    print("The number of occurrences of the first string in the second is:", count_occurrences(substring, string))


if __name__ == "__main__":
    main()
