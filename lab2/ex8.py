#   Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
# True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
#   Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must
# return list of lists.


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
