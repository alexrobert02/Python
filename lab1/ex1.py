# Find The greatest common divisor of multiple numbers read from the console.


def find_gcd(a, b):
    if a == 0:
        return b

    return find_gcd(b % a, a)


def gcd_multiple_numbers(numbers):
    if len(numbers) < 2:
        return "At least two numbers are required to find the GCD."

    gcd = numbers.pop()
    for num in numbers:
        gcd = find_gcd(gcd, num)

    return gcd


def main():
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in input_numbers.split()]

    print("The greatest common divisor of the numbers is:", gcd_multiple_numbers(numbers))


if __name__ == "__main__":
    main()
