import numpy as np
import re
from collections import defaultdict


def one(lines):
    matrix = np.array([list(line) for line in lines])
    state = True
    while True:
        returns = calculate(matrix)
        if returns is None:
            break
        state = returns[0]
        new_matrix = returns[1]
        if (new_matrix == matrix).all():
            break
        else:
            matrix = new_matrix
    print(len(np.where(matrix == 'X')[0]))


def calculate(matrix):
    matrix = matrix.transpose()
    position = np.where(np.logical_or(matrix == '>', matrix == '<'))
    if matrix[position[0], position[1]] == '>':
        line = matrix[position[0]]
        if len(np.where(line == '#')[0]) == 0 or (position[1][0] > np.where(line == '#')[-1]).all():
            matrix[position[0]] = list("".join(line[0][:position[1][0]]) + "".join(['X' for i in range(len(line[0]) - position[1][0])]))
            return True, matrix
        try:
            sub_line = line[0][position[1][0] + 1: np.where(line[0][position[1][0]:] == '#')[-1][0] + 1 + len(line[0]) - len(line[0][position[1][0]:])]
        except IndexError:
            return True, matrix
        sub_line = np.delete(sub_line, np.where(sub_line == '#'))
        if '.' not in sub_line:
            return False, matrix
        matrix[position[0]] = list("".join(line[0][:position[1][0]]) + "".join(['X' for i in range(len(sub_line) + 1)]) + "".join(line[0][np.where(line[0][position[1][0]:] == '#')[-1][0] + len(line[0]) - len(line[0][position[1][0]:]):]))
        matrix[[position[0]], [np.where(line[0][position[1][0]:] == '#')[-1][0] + len(line[0]) - len(line[0][position[1][0]:]) - 1]] = 'v'
        return False, matrix

    if matrix[position[0], position[1]] == '<':
        line = matrix[position[0]]
        if len(np.where(line == '#')[0]) == 0 or np.where(line == '#')[-1].all() > position[1][0]:
            matrix[position[0]] = list("".join(['X' for i in range(position[1][0] + 1)]) + "".join(line[0][position[1][0] + 1:]))
            return True, matrix
        try:
            sub_line = line[0][np.where(line[0][:position[1][0]] == '#')[-1][-1]:position[1][0]]
        except IndexError:
            return True, matrix
        sub_line = np.delete(sub_line, np.where(sub_line == '#'))
        if '.' not in sub_line:
            return False, matrix
        matrix[position[0]] = list("".join(line[0][:np.where(line[0][:position[1][0]] == '#')[-1][-1] + 1]) + "".join(['X' for i in range(len(sub_line) + 1)]) + "".join(line[0][position[1][0] + 1:]))
        matrix[[position[0]], [np.where(line[0][:position[1][0]] == '#')[-1][-1] + 1]] = '^'
        return False, matrix

    # Else transpose
    position = np.where(np.logical_or(matrix == 'v', matrix == '^'))
    if matrix[position[0], position[1]] == 'v':
        line = matrix[position[0]]
        if len(np.where(line == '#')[0]) == 0 or (position[1][0] > np.where(line == '#')[-1]).all():
            matrix[position[0]] = list("".join(line[0][:position[1][0]]) + "".join(['X' for i in range(len(line[0]) - position[1][0])]))
            return True, matrix
        try:
            sub_line = line[0][position[1][0] + 1: np.where(line[0][position[1][0]:] == '#')[-1][0] + 1 + len(line[0]) - len(line[0][position[1][0]:])]
        except IndexError:
            return True, matrix
        sub_line = np.delete(sub_line, np.where(sub_line == '#'))
        if '.' not in sub_line:
            return False, matrix
        matrix[position[0]] = list("".join(line[0][:position[1][0]]) + "".join(['X' for i in range(len(sub_line) + 1)]) + "".join(line[0][np.where(line[0][position[1][0]:] == '#')[-1][0] + len(line[0]) - len(line[0][position[1][0]:]):]))
        matrix[[position[0]], [np.where(line[0][position[1][0]:] == '#')[-1][0] + len(line[0]) - len(line[0][position[1][0]:]) - 1]] = '<'
        return False, matrix

    if matrix[position[0], position[1]] == '^':
        line = matrix[position[0]]
        if len(np.where(line == '#')[0]) == 0 or np.where(line == '#')[-1].all() > position[1][0]:
            matrix[position[0]] = list("".join(['X' for i in range(position[1][0] + 1)]) + "".join(line[0][position[1][0] + 1:]))
            return True, matrix
        try:
            sub_line = line[0][np.where(line[0][:position[1][0]] == '#')[-1][-1]:position[1][0]]
            if '.' not in sub_line:
                return False, matrix
        except IndexError:
            return True, matrix
        sub_line = np.delete(sub_line, np.where(sub_line == '#'))
        matrix[position[0]] = list("".join(line[0][:np.where(line[0][:position[1][0]] == '#')[-1][-1] + 1]) + "".join(['X' for i in range(len(sub_line) + 1)]) + "".join(line[0][position[1][0] + 1:]))
        matrix[[position[0]], [np.where(line[0][:position[1][0]] == '#')[-1][-1] + 1]] = '>'
        return False, matrix


def two(lines):
    matrix = np.array([list(line) for line in lines])
    results = 0
    flip = 0
    while True:
        if flip % 2 == 0:
            results += loop(matrix)
        else:
            results += loop(matrix.transpose())
        flip += 1
        returns = calculate(matrix)
        if returns is None:
            break
        state = returns[0]
        new_matrix = returns[1]
        if (new_matrix == matrix).all():
            break
        else:
            matrix = new_matrix


def loop(matrix):
    results = 0
    # Check if matrix can generate loop
    position = np.where(np.logical_or(matrix == '>', matrix == '<'))
    if matrix[position[0], position[1]] == '>':
        for i in range(position[1][0] + 1, len(matrix[0])):
            if matrix[position[0][0], position[1][0] + i] == '#':
                return results
            matrix_copy = matrix.copy()
            matrix_copy[position[0][0], position[1][0] + i] = '#'
            if complete(matrix_copy):
                results += 1

    elif matrix[position[0], position[1]] == '<':
        for i in range(position[1][0] - 1, 0, -1):
            if matrix[position[0][0], position[1][0] - i] == '#':
                return results
            matrix_copy = matrix.copy()
            matrix_copy[position[0][0], position[1][0] - i] = '#'
            if complete(matrix_copy):
                results += 1

    position = np.where(np.logical_or(matrix == 'v', matrix == '^'))
    if matrix[position[0], position[1]] == 'v':
        for i in range(position[0][0] + 1, len(matrix[0])):
            if matrix[position[0][0] + i, position[1]] == '#':
                return results
            matrix_copy = matrix.copy()
            matrix_copy[position[0][0] + i, position[1][0]] = '#'
            if complete(matrix_copy):
                results += 1

    elif matrix[position[0], position[1]] == '^':
        for i in range(position[0][0] - 1, 0, -1):
            if matrix[position[0][0] - i, position[1][0]] == '#':
                return results
            matrix_copy = matrix.copy()
            matrix_copy[position[0][0] - i, position[1][0]] = '#'
            if complete(matrix_copy):
                results += 1
    return results


def complete(matrix):
    while True:
        returns = calculate(matrix)
        if returns is None:
            break
        state = returns[0]
        new_matrix = returns[1]
        if (new_matrix == matrix).all():
            if not state:
                return True
            break
        else:
            matrix = new_matrix
    return False


def one_v2(lines):
    matrix = np.array([list(line) for line in lines])
    while np.any((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^')):
        matrix = step(matrix)
    print(len(np.where(matrix == 'X')[0]))


def step(matrix):
    position = np.where((matrix == '>') | (matrix == '<'))
    if np.any((matrix[position] == '>') | (matrix[position] == '<')):
        if matrix[position] == '>':
            matrix[position[0]] = list(re.sub(r"(#.*)?(>.*?)(#|$)", lambda m: (m.group(1) or '') + 'X' * (len(m.group(2)) - 1) + ('v' + m.group(3) if m.group(3) == '#' else 'X'), "".join(matrix[position[0]][0])))
        else:
            matrix[position[0]] = list(re.sub(r"(#.*)?(<.*?)(#|$)", lambda m: (m.group(1) or '') + 'X' * (len(m.group(2)) - 1) + ('^' + m.group(3) if m.group(3) == '#' else 'X'), "".join(matrix[position[0]][0])[::-1])[::-1])
        return matrix
    else:
        matrix = matrix.transpose()
        position = np.where((matrix == 'v') | (matrix == '^'))
        if matrix[position] == 'v':
            matrix[position[0]] = list(re.sub(r"(#.*)?(v.*?)(#|$)", lambda m: (m.group(1) or '') + 'X' * (len(m.group(2)) - 1) + ('<' + m.group(3) if m.group(3) == '#' else 'X'), "".join(matrix[position[0]][0])))
        else:
            matrix[position[0]] = list(re.sub(r"(#.*)?(\^.*?)(#|$)", lambda m: (m.group(1) or '') + 'X' * (len(m.group(2)) - 1) + ('>' + m.group(3) if m.group(3) == '#' else 'X'), "".join(matrix[position[0]][0])[::-1])[::-1])
        return matrix.transpose()


def two_v2(lines):
    matrix = np.array([list(line) for line in lines])
    results = 0
    while np.any((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^')):
        if len(np.where((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^'))[0]) > 1:
            test = 0
        results += path(matrix)
        matrix = step(matrix)
    print(results)


def path(matrix):
    results = 0
    position = np.where((matrix == '>') | (matrix == '<'))
    if np.any((matrix[position] == '>') | (matrix[position] == '<')):
        if matrix[position] == '>':
            for string in cases(re.search(r">(.+)", "".join(matrix[position[0]][0]))[0][1:]):
                matrix_copy = matrix.copy()
                matrix_copy[position[0]] = np.array(list(re.search("(.+)>", "".join(matrix[position[0]][0]))[0] + string))
                if cycle(matrix_copy):
                    results += 1
        else:
            for string in cases(re.search(r"(.+)<", "".join(matrix[position[0]][0]))[0][:-1][::-1]):
                matrix_copy = matrix.copy()
                matrix_copy[position[0]] = np.array(list(string[::-1] + re.search("<(.+)", "".join(matrix[position[0]][0]))[0]))
                if cycle(matrix_copy):
                    results += 1
        return results
    else:
        matrix = matrix.transpose()
        position = np.where((matrix == 'v') | (matrix == '^'))
        if matrix[position] == 'v':
            for string in cases(re.search(r"v(.+)", "".join(matrix[position[0]][0]))[0][1:]):
                matrix_copy = matrix.copy()
                matrix_copy[position[0]] = np.array(list(re.search(r"(.+)v", "".join(matrix[position[0]][0]))[0] + string))
                if cycle(matrix_copy.transpose()):
                    results += 1
        else:
            for string in cases(re.search(r"(.+)\^", "".join(matrix[position[0]][0]))[0][:-1][::-1]):
                matrix_copy = matrix.copy()
                matrix_copy[position[0]] = np.array(list(string[::-1] + re.search(r"\^(.+)", "".join(matrix[position[0]][0]))[0]))
                if len(np.where((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^'))[0]) > 1 or len(np.where((matrix_copy == '>') | (matrix_copy == '<') | (matrix_copy == 'v') | (matrix_copy == '^'))[0]) > 1:
                    test = 0
                if cycle(matrix_copy.transpose()):
                    results += 1
        return results


def cases(string):
    string_list = []
    for char in range(len(string)):
        if string[char] != '#':
            string_copy = list(string)
            string_copy[char] = '#'
            string_list.append("".join(string_copy))
        else:
            break
    return string_list


def cycle(matrix):
    corners = {'>': [], '<': [], '^': [], 'v': []}
    while np.any((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^')):
        position = np.where((matrix == '>') | (matrix == '<') | (matrix == 'v') | (matrix == '^'))
        try:
            if position in corners[matrix[position][0]]:
                return True
        except ValueError:
            test = 0
        corners[matrix[position][0]].append((position[0], position[1]))
        matrix = step(matrix)
    return False

if __name__ == '__main__':
    fileInput = open("input/Day6.txt", "r").read()
    # one(fileInput.split("\n"))
    # two(fileInput.split("\n"))
    # one_v2(fileInput.split("\n"))
    two_v2(fileInput.split("\n"))
