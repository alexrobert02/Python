def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for num in numbers:
        if is_palindrome(num):
            palindrome_count += 1
            if greatest_palindrome is None or num > greatest_palindrome:
                greatest_palindrome = num

    return palindrome_count, greatest_palindrome


def main():
    numbers = [121, 123, 1331, 555, 656, 8448, 525]
    print(find_palindromes(numbers))


if __name__ == '__main__':
    main()
