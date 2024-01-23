def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix) or not middle in value[1:-1] or not value.endswith(suffix):
                return False
        else:
            return False
    return True


def main():
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    data = {"key1": "come inside, it's too cold out", "key3": "start with middle and winter"}
    print(validate_dict(rules, data))


if __name__ == '__main__':
    main()
