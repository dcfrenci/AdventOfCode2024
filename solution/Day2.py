import numpy as np


def safe(lines):
    results = 0
    for line in lines:
        array = np.array(line.split(" "), dtype=int)
        if check(array):
            results += 1
    print(results)

def safer(lines):
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


if __name__ == '__main__':
    fileInput = open("input/Day2.txt", "r").read()
    safe(fileInput.split("\n"))
    safer(fileInput.split("\n"))
