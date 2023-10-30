#   Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be
# recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)


def dict_compare(dict1, dict2):
    if type(dict1) is not dict or type(dict2) is not dict:
        return dict1 == dict2

    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False
        if not dict_compare(dict1[key], dict2[key]):
            return False

    return True


def main():
    dict1 = {
        "a": 1,
        "b": [2, 3, {"c": 4}],
        "d": {"e": 5, "f": [6, 7]}
    }

    dict2 = {
        "a": 1,
        "b": [2, 3, {"c": 4}],
        "d": {"e": 5, "f": [6, 7]}
    }

    dict3 = {
        "a": 1,
        "b": [2, 3, {"c": 4}],
        "d": {"e": 5, "f": [6, 8]}
    }

    print(dict_compare(dict1, dict2))
    print(dict_compare(dict1, dict3))


if __name__ == '__main__':
    main()
