def find_obstructed_seats(matrix):
    obstructed_seats = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(num_cols):
        for row in range(num_rows - 1):
            for upper_row in range(row + 1, num_rows):
                if matrix[upper_row][col] <= matrix[row][col] and (upper_row, col) not in obstructed_seats:
                    obstructed_seats.append((upper_row, col))

    return obstructed_seats


def main():
    stadium_matrix = [[1, 2, 3, 2, 1, 1],
                      [2, 4, 4, 3, 7, 2],
                      [5, 5, 2, 5, 6, 4],
                      [6, 6, 7, 6, 7, 5]]

    print(find_obstructed_seats(stadium_matrix))


if __name__ == '__main__':
    main()
