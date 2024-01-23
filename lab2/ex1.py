def fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    while len(fibonacci_list) < n:
        fibonacci_list.append(a)
        a, b = b, a+b
    return fibonacci_list


def main():
    n = 8
    print(f"The first {n} numbers in the Fibonacci string:", fibonacci(n))


if __name__ == '__main__':
    main()
