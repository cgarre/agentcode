import sys


def sort_list(numbers):
    return sorted(numbers)


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(sort_list(nums))
