def find_items_appearing_x_times(x, *lists):
    combined_list = []
    for sublist in lists:
        combined_list.extend(sublist)

    item_counts = {}
    result = []

    for item in combined_list:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    for item, count in item_counts.items():
        if count == x:
            result.append(item)

    return result


def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]

    print(find_items_appearing_x_times(2, list1, list2, list3, list4))


if __name__ == '__main__':
    main()
