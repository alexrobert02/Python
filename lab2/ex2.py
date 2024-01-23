def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def find_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Prime numbers:", find_primes(numbers))


if __name__ == '__main__':
    main()
