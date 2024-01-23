def compose(notes, moves, start_position):
    song = [notes[start_position]]
    current_position = start_position

    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])

    return song


def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2

    print(compose(notes, moves, start_position))


if __name__ == '__main__':
    main()
