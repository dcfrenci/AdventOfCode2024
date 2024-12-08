import string
import numpy as np
from itertools import combinations
from collections import defaultdict


def one(lines):
    matrix = np.array([list(line) for line in lines])
    position = defaultdict(list)
    for letter in list(string.ascii_lowercase + string.ascii_uppercase + string.digits):
        if np.any(matrix == letter):
            position[letter] = list(zip(np.where(matrix == letter)[0], np.where(matrix == letter)[1]))
    anti_nodes = set()
    for letter in position:
        for combination in combinations(position[letter], 2):
            line = combination[0][0] - combination[1][0]
            column = combination[0][1] - combination[1][1]
            for node in ((combination[0][0] + line, combination[0][1] + column), (combination[1][1] - line, combination[1][1] - column)):
                if check(node, len(matrix[0])):
                    anti_nodes.add(node)
    print(len(anti_nodes))


def check(node, length):
    if node[0] < 0 or node[0] >= length:
        return False
    if node[1] < 0 or node[1] >= length:
        return False
    return True


def two(lines):
    matrix = np.array([list(line) for line in lines])
    position = defaultdict(list)
    for letter in list(string.ascii_lowercase + string.ascii_uppercase + string.digits):
        if np.any(matrix == letter):
            position[letter] = list(zip(np.where(matrix == letter)[0], np.where(matrix == letter)[1]))
    anti_nodes = set()
    for letter in position:
        for combination in combinations(position[letter], 2):
            for node in generate_nodes(combination[0], combination[1], len(matrix[0])):
                if check(node, len(matrix[0])):
                    anti_nodes.add(node)
    print(len(anti_nodes))


def generate_nodes(n1, n2, length):
    nodes = []
    line = n1[0] - n2[0]
    column = n1[1] - n2[1]
    while True:
        nodes.append(n1)
        nodes.append(n2)
        n1 = (n1[0] + line, n1[1] + column)
        n2 = (n2[0] - line, n2[1] - column)
        if not check(n1, length) and not check(n2, length):
            break
    return nodes


if __name__ == '__main__':
    fileInput = open("input/Day8.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
