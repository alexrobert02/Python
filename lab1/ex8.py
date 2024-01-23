def count_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


def main():
    number = 24
    print(f"Number of set bits in {number}: {count_bits(number)}")


if __name__ == "__main__":
    main()
