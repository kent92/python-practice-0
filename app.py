from numbers_qwe import *
from math import *


def main():
    print("Hello, World!")


def solve_problem(a: int, b: int) -> int:
    c = multiply_two_numbers(a, b)
    return a + b + c


def calculate_circle_area(radius) -> object:
    return pi * radius**2


if __name__ == '__main__':
    print(solve_problem(4, 5))
    print(divide_two_numbers(5, 4))
    print(calculate_circle_area(2.6317))
    main()
