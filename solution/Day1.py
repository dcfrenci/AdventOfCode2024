import numpy as np


def one(lines):
    first, second = [], []
    for line in lines:
        first.append(int(line.split()[0]))
        second.append(int(line.split()[-1]))
    print(abs(np.array(sorted(first)) - np.array(sorted(second))).sum())


def two(lines):
    first, second = [], []
    for line in lines:
        first.append(int(line.split()[0]))
        second.append(int(line.split()[-1]))
    result = 0
    for i in range(len(first)):
        result += first[i] * second.count(first[i])
    print(result)


if __name__ == '__main__':
    fileInput = open("input/Day1.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
