import sys


def sort_list(numbers):
    return sorted(numbers)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python sort_list.py <int> [<int> ...]")
        sys.exit(1)

    try:
        nums = [int(value) for value in sys.argv[1:]]
    except ValueError:
        print("Error: all arguments must be integers.")
        sys.exit(1)

    print(" ".join(map(str, sort_list(nums))))
