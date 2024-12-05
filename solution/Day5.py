import numpy as np
from collections import defaultdict
import timeit


def one(lines):
    rules = defaultdict(list)
    [rules[line.split("|")[0]].append(line.split("|")[1]) for line in lines[:lines.index("")]]
    return sum([int(line.split(",")[int((len(line.split(",")) - 1) / 2)]) for line in lines[lines.index("") + 1:] if control(rules, line.split(","), False)])


def two(lines):
    rules = defaultdict(list)
    [rules[line.split("|")[0]].append(line.split("|")[1]) for line in lines[:lines.index("")]]
    return sum([int(control(rules, line.split(","), True)[int((len(line.split(",")) - 1) / 2)]) for line in lines[lines.index("") + 1:] if control(rules, line.split(","), True)]) - one(lines)


def control(rules, array, correction):
    for element in array:
        for this in array[array.index(element) + 1:]:
            if this not in rules[element]:
                if correction:
                    if array.index(element) == len(array) - 1:
                        return []
                    swapped = array.copy()
                    swapped[array.index(element)], swapped[array.index(this)] = swapped[array.index(this)], swapped[array.index(element)]
                    return control(rules, swapped, correction)
                return []
    return array


if __name__ == '__main__':
    fileInput = open("input/Day5.txt", "r").read()
    print(one(fileInput.split("\n")))
    execution_time = timeit.timeit(lambda: one(fileInput.split("\n")), number=1)
    print(f"Execution time: {execution_time / 10:.6f} second")
    print(two(fileInput.split("\n")))
    execution_time = timeit.timeit(lambda: two(fileInput.split("\n")), number=1)
    print(f"Execution time: {execution_time / 10:.6f} second")
