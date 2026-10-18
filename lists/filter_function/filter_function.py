from typing import Callable


def filter_list(l: list, condition: Callable) -> list:
    result = []
    for x in l:
        if condition(x):
            result.append(x)
    return result


def filter_list2(l: list, condition: Callable) -> list:
    return [x for x in l if condition(x)]


if __name__ == "__main__":

    def is_even(x):
        return x % 2 == 0

    print(filter_list([11, 4, 7, 22, 9], is_even))  # [4, 22]
