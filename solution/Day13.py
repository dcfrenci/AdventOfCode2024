import re
import numpy as np
from sympy import divisors
from itertools import product


def one(machines):
    results = 0
    for machine in machines:
        numbers = [int(number) for number in re.findall(r"(\d+)", machine)]
        a_button, b_button, price = (numbers[0], numbers[1]), (numbers[2], numbers[3]), (numbers[4], numbers[5])
        results += combination(a_button, b_button, price)
    print(results)


def two(machines):
    results = 0
    for machine in machines:
        numbers = [int(number) for number in re.findall(r"(\d+)", machine)]
        a_button, b_button, price = (numbers[0], numbers[1]), (numbers[2], numbers[3]), (numbers[4] + 10000000000000, numbers[5] + 10000000000000)
        det = a_button[0] * b_button[1] - a_button[1] * b_button[0]
        if det == 0 or (a_button[0] * price[1] - b_button[0] * price[0]) % det != 0 or (b_button[1] * price[0] - a_button[1] * price[1]) % det != 0:
            continue
        results += ((b_button[1] * price[0] - a_button[1] * price[1]) / det) * 3 + (a_button[0] * price[1] - b_button[0] * price[0]) / det
    print(results)


def trova_soluzione(delta, v1, v2):
    # Esegui una ricerca per trovare lambda1 e lambda2 interi
    for lambda1 in range(-100, 100):  # Limita la ricerca per valori di lambda1
        for lambda2 in range(-100, 100):  # Limita la ricerca per valori di lambda2
            if np.array_equal(lambda1 * v1 + lambda2 * v2, delta):
                return lambda1, lambda2
    return 0, 0


def combination(a_button, b_button, price):
    solution = []
    for part in range(100):
        for i in range(100):
            if (a_button[0] * part + b_button[0] * i, a_button[1] * part + b_button[1] * i) == price:
                solution.append(3 * part + i)
            if (a_button[0] * i + b_button[0] * part, a_button[1] * i + b_button[1] * part) == price:
                solution.append(3 * i + part)
    return sorted(solution)[0] if len(solution) > 0 else 0


if __name__ == '__main__':
    fileInput = open("input/Day13.txt", "r").read()
    # one(fileInput.split("\n\n"))
    two(fileInput.split("\n\n"))

# def backtrack(a_rep, b_rep):
#     position = (a_rep * a_button[0] + b_rep * b_button[0], a_rep * a_button[1] + b_rep * b_button[1])
#     if a_rep > 100 or b_rep > 100 or position[0] > price[0] or position[1] > price[1]:
#         return
#     if len(solution) > 0 and 3 * a_rep + b_rep > sorted(solution)[0]:
#         return
#     if position == price:
#         solution.append(3 * a_rep + b_rep)
#         return
#     backtrack(a_rep, b_rep + 1)
#     backtrack(a_rep + 1, b_rep)
#
# backtrack(0, 0)
# return sorted(solution)[0]
# def combination(a_button, b_button, price):
#     solution = []
#     partition = list(set(divisors(price[0]) + divisors(price[1])))
#     for part in range(100):
#         for i in range(100):
#             if (a_button[0] * part + b_button[0] * i, a_button[1] * part + b_button[1] * i) == price:
#                 solution.append(3 * part + i)
#             if (a_button[0] * i + b_button[0] * part, a_button[1] * i + b_button[1] * part) == price:
#                 solution.append(3 * i + part)
#     return sorted(solution)[0] if len(solution) > 0 else 0