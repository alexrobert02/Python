def list_operations(a, b):
    intersection = []
    union = []
    a_minus_b = []
    b_minus_a = []

    for item in a:
        if item in b:
            intersection.append(item)
        union.append(item)

    for item in b:
        if item not in a:
            union.append(item)
            b_minus_a.append(item)

    for item in a:
        if item not in b:
            a_minus_b.append(item)

    return intersection, union, a_minus_b, b_minus_a


def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

    result = list_operations(a, b)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("a - b:", result[2])
    print("b - a:", result[3])


if __name__ == '__main__':
    main()
