import numpy as np
import re

from numpy.ma.core import append


def one(lines):
    results = 0
    for line in lines:
        array = np.array(line.split(" "), dtype=int)
        if check(array):
            results += 1
    print(results)


def two(lines):
    results = 0
    for line in lines:
        array = np.array(line.split(" "), dtype=int)
        if check(array):
            results += 1
        else:
            for i in range(len(array)):
                if check(np.delete(array, i)):
                    results += 1
                    break
    print(results)


def check(array):
    array_sorted = sorted(array)
    if (array == array_sorted).all() or (array_sorted[::-1] == array).all():
        for i in range(len(array) - 1):
            if array[i + 1] - array[i] > 3 or array[i + 1] - array[i] <= 0:
                return False
        return True
    return False


def one_library(lines):
    # array = np.array([list(line.split(" ")) for line in lines])
    array = [line.split(" ") for line in lines]
    return len([report for report in array if report == sorted(report) or report == sorted(report)[::-1]
                if [1 for level in report if level]])
    # return len([report for report in array if report == np.sort(report) or report == np.sort(report)[::-1]])


if __name__ == '__main__':
    fileInput = open("input/Day2.txt", "r").read()
    one(fileInput.split("\n"))
    print(one_library(fileInput.split("\n")))
    # two(fileInput.split("\n"))
