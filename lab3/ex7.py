def set_operations(*sets):
    results = {}

    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            set1, set2 = sets[i], sets[j]

            # Union
            key = f"{set1} | {set2}"
            results[key] = set1.union(set2)

            # Intersection
            key = f"{set1} & {set2}"
            results[key] = set1.intersection(set2)

            # Set difference: A - B
            key = f"{set1} - {set2}"
            results[key] = set1.difference(set2)

            # Set difference: B - A
            key = f"{set2} - {set1}"
            results[key] = set2.difference(set1)

    return results


def main():
    set1 = {1, 2}
    set2 = {2, 3}
    result = set_operations(set1, set2)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()
