def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

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
