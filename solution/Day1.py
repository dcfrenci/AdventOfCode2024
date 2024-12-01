import numpy as np


def distance(lines):
    firstColumn = []
    secondColumn = []
    for line in lines:
        split = line.split(" ")
        firstColumn.append(split[0])
        secondColumn.append(split[len(split) - 1])

    firstColumn = sorted(np.array(firstColumn, dtype=int))
    secondColumn = sorted(np.array(secondColumn, dtype=int))
    results = 0
    for i in range(len(firstColumn)):
        results += abs(firstColumn[i] - secondColumn[i])
    print(results)


def frequency(lines):
    firstColumn = []
    secondColumn = []
    for line in lines:
        split = line.split(" ")
        firstColumn.append(int(split[0]))
        secondColumn.append(int(split[len(split) - 1]))
    results = 0
    for i in range(len(firstColumn)):
        results += firstColumn[i] * secondColumn.count(firstColumn[i])
    print(results)


if __name__ == '__main__':
    fileInput = open("input/Day1.txt", "r").read()
    distance(fileInput.split("\n"))
    frequency(fileInput.split("\n"))
