from Queue import Queue


def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    print("Queue:", queue.items)
    print("Pop:", queue.pop())
    print("Peek:", queue.peek())
    print("Is empty:", queue.is_empty())
    print("Size:", queue.size())


if __name__ == '__main__':
    main()
