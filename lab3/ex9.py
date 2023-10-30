#   Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# and will return the number of positional arguments whose values can be found among keyword arguments values. Ex:
# my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3


def count_matching_values(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count


def main():
    print("The number of matching values:", count_matching_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == '__main__':
    main()
