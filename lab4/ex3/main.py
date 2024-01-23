from Matrix import Matrix


def main():
    matrix = Matrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("\nMatrix:")
    for i in range(matrix.n):
        for j in range(matrix.m):
            print(matrix.get(i, j), end=" ")
        print()

    transposed = matrix.transpose()
    print("\nTransposed matrix:")
    for i in range(transposed.n):
        for j in range(transposed.m):
            print(transposed.get(i, j), end=" ")
        print()

    other = Matrix(3, 2)
    other.set(0, 0, 7)
    other.set(0, 1, 8)
    other.set(1, 0, 9)
    other.set(1, 1, 10)
    other.set(2, 0, 11)
    other.set(2, 1, 12)

    multiplied = matrix.multiply(other)
    print("\nMultiplication of both matrix:")
    for i in range(multiplied.n):
        for j in range(multiplied.m):
            print(multiplied.get(i, j), end=" ")
        print()

    matrix.transform(lambda x: x * 2)
    print("\nTransformed matrix:")
    for i in range(matrix.n):
        for j in range(matrix.m):
            print(matrix.get(i, j), end=" ")
        print()


if __name__ == '__main__':
    main()
