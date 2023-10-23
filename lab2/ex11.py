#   Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


def custom_sort(tuple_list):
    sorted_list = sorted(tuple_list, key=lambda item: item[1][2])
    return sorted_list


def main():
    tuple_list = [('abc', 'bcd'), ('abc', 'zza')]
    print(custom_sort(tuple_list))


if __name__ == '__main__':
    main()
