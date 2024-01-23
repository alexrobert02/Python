def filter_strings(x=1, string_list=[], flag=True):
    result = []

    for s in string_list:
        filtered_chars = []

        for char in s:
            if (flag and ord(char) % x == 0) or (not flag and ord(char) % x != 0):
                filtered_chars.append(char)

        result.append(filtered_chars)

    return result


def main():
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    print(filter_strings(x, strings, flag))


if __name__ == '__main__':
    main()
