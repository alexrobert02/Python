#   Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].
#   Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to
# generate max ([len(x) for x in input_lists]) tuples.


def combine_lists(*input_lists):
    max_length = max ([len(x) for x in input_lists])
    for input_list in input_lists:
        if len(input_list) != max_length:
            input_list.extend([None] * (max_length - len(input_list)))

    return list(zip(*input_lists))


def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]

    print(combine_lists(list1, list2, list3))


if __name__ == '__main__':
    main()
