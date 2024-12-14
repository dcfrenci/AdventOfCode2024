import re
import numpy as np
import shutil
import os
# import aspose-words as aw
# import PIL
# from PIL import Image
import matplotlib.pyplot as plt
# from pathlib import Path
# from pygments.formatters import ImageFormatter
# import pygments.lexers


def one(lines):
    matrix = np.zeros((103, 101))
    for line in lines:
        numbers = [int(number) for number in re.findall(r"(\d+|-\d+)", line)]
        positions, velocity = (numbers[0], numbers[1]), (numbers[2], numbers[3])
        for time in range(100):
            positions = calculate(positions, velocity, matrix)
        matrix[positions[1], positions[0]] += 1
    horizontal, vertical = int((len(matrix) - 1) / 2), int((len(matrix[0]) - 1) / 2)
    results = 0
    for quadrant in [matrix[:horizontal, :vertical], matrix[:horizontal, vertical + 1:], matrix[horizontal + 1:, :vertical], matrix[horizontal + 1:, vertical + 1:]]:
        if results == 0:
            results = quadrant.sum()
        else:
            results *= quadrant.sum()
    print(results)


def two(lines):
    matrix = np.full((103, 101), 0)
    robots = []
    for line in lines:
        numbers = [int(number) for number in re.findall(r"(\d+|-\d+)", line)]
        positions, velocity = (numbers[0], numbers[1]), (numbers[2], numbers[3])
        robots.append([(numbers[0], numbers[1]), (numbers[2], numbers[3])])

        positions = calculate(positions, velocity, matrix)
        matrix[positions[1], positions[0]] += 1
    second = 0
    for filename in os.listdir('output/Day14'):
        if 'second' in filename:
            os.remove(os.path.join('output/Day14', filename))
    while True:
        new_robot = []
        for robot in robots:
            positions, velocity = robot[0], robot[1]
            if matrix[positions[1], positions[0]] > 0:
                matrix[positions[1], positions[0]] -= 1
            positions = calculate(positions, velocity, matrix)
            matrix[positions[1], positions[0]] = 1
            new_robot.append([positions, velocity])
        second += 1
        with open('output/Day14/text.txt', 'w') as file:
            pass
        string = ""
        for line in matrix:
            string = string + "\n" + "".join(str(char) for char in line)

        with open('output/Day14/text.txt', 'w') as f:
            print(string.replace('0', '.'), file=f)

        if close_robots(matrix):
            txt_to_image(second)
        robots = new_robot
        if second == 10000:
            return


def close_robots(matrix):
    configuration = np.full((8, 8), 1)
    n, m = matrix.shape
    p, q = configuration.shape

    for i in range(n - p + 1):
        for j in range(m - q + 1):
            if np.array_equal(matrix[i:i+p, j:j+q], configuration):
                return True
    return False


def calculate(positions, velocity, matrix):
    if 0 <= positions[0] + velocity[0] < len(matrix[0]) and 0 <= positions[1] + velocity[1] < len(matrix):
        return positions[0] + velocity[0], positions[1] + velocity[1]

    if positions[0] + velocity[0] >= len(matrix[0]):
        if positions[1] + velocity[1] >= len(matrix):
            return positions[0] + velocity[0] - len(matrix[0]), positions[1] + velocity[1] - len(matrix)
        if positions[1] + velocity[1] < 0:
            return positions[0] + velocity[0] - len(matrix[0]), len(matrix) + positions[1] + velocity[1]
        if positions[1] + velocity[1] == 0:
            return positions[0] + velocity[0] - len(matrix[0]), positions[1] + velocity[1]
        return positions[0] + velocity[0] - len(matrix[0]), positions[1] + velocity[1]

    if positions[0] + velocity[0] < 0:
        if positions[1] + velocity[1] >= len(matrix):
            return len(matrix[0]) + positions[0] + velocity[0], positions[1] + velocity[1] - len(matrix)
        if positions[1] + velocity[1] < 0:
            return len(matrix[0]) + positions[0] + velocity[0], len(matrix) + positions[1] + velocity[1]
        if positions[1] + velocity[1] == 0:
            return len(matrix[0]) + positions[0] + velocity[0], positions[1] + velocity[1]
        return len(matrix[0]) + positions[0] + velocity[0], positions[1] + velocity[1]

    if positions[1] + velocity[1] >= len(matrix):
        return positions[0] + velocity[0], positions[1] + velocity[1] - len(matrix)
    if positions[1] + velocity[1] < 0:
        return positions[0] + velocity[0], len(matrix) + positions[1] + velocity[1]
    if positions[1] + velocity[1] == 0:
        return positions[0] + velocity[0], positions[1] + velocity[1]
    return positions[0] + velocity[0], positions[1] + velocity[1]


def txt_to_image(second):
    file_txt = "output/Day14/text.txt"
    file_png = f"output/Day14/second_{second}.png"
    with open(file_txt, "r", encoding="utf-8") as file:
        content = file.read()
    plt.figure(figsize=(10, 8))
    plt.text(0.5, 0.5, content, fontsize=12, ha="center", va="center", wrap=True)
    plt.axis('off')
    plt.savefig(file_png, bbox_inches='tight', dpi=200)
    plt.close()


if __name__ == '__main__':
    fileInput = open("input/Day14.txt", "r").read()
    # one(fileInput.split("\n"))
    two(fileInput.split("\n"))
