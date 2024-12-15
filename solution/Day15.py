import numpy as np
import re


def one(lines):
    matrix = np.array([list(line) for line in lines[0].split('\n')])
    for char in lines[1].replace('\n', ''):
        matrix = make_move(char, matrix)
    print(sum(position[0] * 100 + position[1] for position in list(zip(np.where(matrix == 'O')[0], np.where(matrix == 'O')[1]))))


def two(lines):
    matrix = np.array([list(line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for line in lines[0].split('\n')])
    for char in lines[1].replace('\n', ''):
        matrix = make_big_move(1 if char == 'v' else - 1, matrix) if char == 'v' or char == '^' else make_move(char, matrix)
    print(sum(position[0] * 100 + position[1] for position in list(zip(np.where(matrix == '[')[0], np.where(matrix == '[')[1]))))


def make_big_move(line, matrix):
    position = np.where(matrix == '@')
    move, positions = calculate_big(matrix, position, line)
    if move:
        matrix_copy = matrix.copy()
        boxes = []
        for coordinates in positions:
            if position not in boxes:
                boxes.append(coordinates)
                matrix_copy[coordinates] = '.'
        for box in boxes:
            if matrix[box] == '[' or matrix[box] == ']':
                matrix_copy[box[0] + line, box[1]] = matrix[box]
        matrix_copy[position], matrix_copy[position[0] + line, position[1]] = '.', '@'
        return matrix_copy
    return matrix


def calculate_big(matrix, position, down):
    previous_line = [(position[0] + down, position[1])]
    if matrix[(position[0] + down, position[1])] == '[' or matrix[(position[0] + down, position[1])] == ']':
        previous_line.append((position[0] + down, position[1] + 1) if matrix[(position[0] + down, position[1])] == '[' else (position[0] + down, position[1] - 1))
    boxes = previous_line
    while True:
        new_boxes = []
        for box in previous_line:
            if matrix[box] == '#':
                return False, boxes
            if matrix[box] == '[':
                for index in range(0, 2):
                    new_boxes.append((box[0] + down, box[1] + index))
                    if matrix[box[0] + down, box[1] + index] == ']' and index == 0:
                        new_boxes.append((box[0] + down, box[1] + index - 1))
                    if matrix[box[0] + down, box[1] + index] == '[' and index == 1:
                        new_boxes.append((box[0] + down, box[1] + index + 1))
        if len(new_boxes) == 0:
            return True, boxes
        boxes.extend(new_boxes)
        previous_line = new_boxes


def make_move(char, matrix):
    position = np.where(matrix == '@')
    if char == '>' or char == '<':
        if char == '>':
            matrix[position[0]] = list(calculate("".join(matrix[position[0]][0])))
        else:
            matrix[position[0]] = list(calculate("".join(matrix[position[0]][0])[::-1])[::-1])
        return matrix
    return make_move('>' if char == 'v' else '<', matrix.transpose()).transpose()


def calculate(string):
    return re.sub(r"(#.*)(@.*?)(#|$)", lambda m: m.group(1) + ('.' + '@' + re.sub(r"(@.*?)(\.)(.*)", lambda k: k.group(1)[1:] + k.group(3), m.group(2)) if len(re.findall(r"\.", m.group(2))) != 0 else m.group(2)) + m.group(3), string)


if __name__ == '__main__':
    fileInput = open("input/Day15.txt", "r").read()
    one(fileInput.split("\n\n"))
    two(fileInput.split("\n\n"))

