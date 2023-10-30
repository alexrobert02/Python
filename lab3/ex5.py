#   The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise.
#   Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules
# are respected for "key1" and "key2" "key3" that does not appear in the rules.


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
