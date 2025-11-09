from typing import Callable


def filter_list(lst: list, condition: Callable) -> list:
    return [x for x in lst if condition(x)]


if __name__ == "__main__":
    # Test your function
    def is_even(x):
        return x % 2 == 0


    print(filter_list([1, 2, 3, 4, 5, 6], is_even))  # [2, 4, 6]


    def is_positive(x):
        return x > 0


    print(filter_list([-2, -1, 0, 1, 2], is_positive))  # [1, 2]
