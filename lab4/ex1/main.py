from Stack import Stack


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack.items)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Is empty:", stack.is_empty())
    print("Size:", stack.size())
    print()


if __name__ == '__main__':
    main()
