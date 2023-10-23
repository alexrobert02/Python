#   Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
#
#   Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte',
# 'parte'], ['arme']]


def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        rhyme = word[-2:]

        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]

    return list(rhyme_groups.values())


def main():
    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    print(group_by_rhyme(words))


if __name__ == '__main__':
    main()
