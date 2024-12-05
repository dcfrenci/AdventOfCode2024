import numpy as np
import re
from numpy.lib.stride_tricks import sliding_window_view


def one(lines):
    matrix = np.array([list(line) for line in lines])
    return calculate(matrix) + calculate(matrix.transpose()) + calc_diagonal(matrix) + calc_diagonal(np.fliplr(matrix))


def calculate(matrix):
    return sum([len(re.findall(r"XMAS", "".join(line)) + re.findall(r"SAMX", "".join(line))) for line in matrix])


def calc_diagonal(matrix):
    return (sum([len(re.findall(r"XMAS", "".join(np.diag(matrix, diagonal))) +
                     re.findall(r"SAMX", "".join(np.diag(matrix, diagonal)))) for diagonal in range(len(matrix))])
            + sum([len(re.findall(r"XMAS", "".join(np.diag(matrix, diagonal - len(matrix))))
                       + re.findall(r"SAMX", "".join(np.diag(matrix, diagonal - len(matrix))))) for diagonal in
                   range(len(matrix))]))


def two(lines):
    matrix = np.array([list(line) for line in lines])
    sub_matrix_list = sliding_window_view(matrix, (3, 3)).reshape(-1, 3, 3)
    return len([sub_matrix for sub_matrix in sub_matrix_list if
                "".join(np.diag(sub_matrix)) == "MAS" or "".join(np.diag(sub_matrix)) == "SAM"
                if "".join(np.diag(np.fliplr(sub_matrix))) == "MAS" or "".join(np.diag(np.fliplr(sub_matrix))) == "SAM"])


if __name__ == '__main__':
    fileInput = open("input/Day4.txt", "r").read()
    print(one(fileInput.split("\n")))
    print(two(fileInput.split("\n")))
