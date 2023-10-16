# Write a script that receives two strings and prints the number of occurrences of the first string in the second.


def count_occurences(substring, string):
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

    print("The number of occurences of the first string in the second is:", count_occurences(substring, string))


if __name__ == "__main__":
    main()
