def custom_sort(tuple_list):
    sorted_list = sorted(tuple_list, key=lambda item: item[1][2])
    return sorted_list


def main():
    tuple_list = [('abc', 'bcd'), ('abc', 'zza')]
    print(custom_sort(tuple_list))


if __name__ == '__main__':
    main()
