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
