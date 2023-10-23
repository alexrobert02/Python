#   Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A
# spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
# occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
# row from the field.
#
# 	Example:
#
#   # FIELD
#
#   [[1, 2, 3, 2, 1, 1],
#
#   [2, 4, 4, 3, 7, 2],
#
#   [5, 5, 2, 5, 6, 4],
#
#   [6, 6, 7, 6, 7, 5]]
#
#   Will return : [(2, 2), (3, 4), (2, 4)]


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
