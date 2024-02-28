from math import sqrt
from typing import Optional

num_x: int = 10
num_y: int = 5


def add_numbers(num_x: int, num_y: int) -> int:
    return num_x + num_y


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    else:
        roots: float = calculate_square_root(your_number)
        return ('Мы вычислили квадратный корень из '
                'введённого вами числа. Это будет:' + str(roots))


def calculate_square_root(num: float) -> float:
    return sqrt(num)


print('Сумма чисел:', add_numbers(num_x, num_y))
print(calc(25.5))
