#   Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique
# elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this
# objective).


def count_unique_and_duplicates(input_list):
    unique_set = set()
    duplicate_set = set()

    for item in input_list:
        if item in unique_set:
            duplicate_set.add(item)
        else:
            unique_set.add(item)

    return len(unique_set), len(duplicate_set)


def main():
    input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    result = count_unique_and_duplicates(input_list)
    print("Unique elements:", result[0])
    print("Duplicate elements:", result[1])


if __name__ == '__main__':
    main()
