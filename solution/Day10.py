import numpy as np


def one(lines):
    matrix = np.array([list(line) for line in lines])
    print(sum(len(set(paths(matrix, trailhead, []))) for trailhead in list(zip(np.where(matrix == '0')[0], np.where(matrix == '0')[1]))))


def two(lines):
    matrix = np.array([list(line) for line in lines])
    print(sum(len(paths(matrix, trailhead, [])) for trailhead in list(zip(np.where(matrix == '0')[0], np.where(matrix == '0')[1]))))


def paths(topographic_map, trailhead, results):
    def backtrack(matrix, position):
        if int(matrix[position]) == 9:
            return results.append(position)
        for neighbour in neighbours(matrix, position):
            if int(matrix[neighbour]) == int(matrix[position]) + 1:
                backtrack(matrix, neighbour)

    backtrack(topographic_map, trailhead)
    return results


def neighbours(matrix, position):
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    return [(position[0] + offset[0], position[1] + offset[1]) for offset in offsets if 0 <= position[0] + offset[0] < len(matrix[0]) and 0 <= position[1] + offset[1] < len(matrix[0])]


if __name__ == '__main__':
    fileInput = open("input/Day10.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
