def is_palindrome(number):
    temp = number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10

    return temp == reverse_number


def main():
    input_number = int(input("Enter a number: "))
    print(f"Is {input_number} palindrome?", is_palindrome(input_number))


if __name__ == "__main__":
    main()
