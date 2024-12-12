import numpy as np
import string
from collections import defaultdict


def one(lines):
    matrix = np.array([list(line) for line in lines])
    regions = defaultdict(list)
    for key in list(string.ascii_uppercase):
        if np.any(matrix == key):
            regions[key] = list(zip(np.where(matrix == key)[0], np.where(matrix == key)[1]))
    print(sum(len(group) * perimeter(group) for key in regions.keys() for group in make_group(regions[key], [])))


def two(lines):
    matrix = np.array([list(line) for line in lines])
    regions = defaultdict(list)
    for key in list(string.ascii_uppercase):
        if np.any(matrix == key):
            regions[key] = list(zip(np.where(matrix == key)[0], np.where(matrix == key)[1]))
    print(sum(len(group) * side(group) for key in regions.keys() for group in make_group(regions[key], [])))


def make_group(points_list, groups):
    def backtrack(points, group):
        if len(points) == 0:
            return groups.append(group)
        new_group = []
        for element in group:
            for point in points:
                if point[0] == element[0]:
                    if point[1] == element[1] + 1 or point[1] == element[1] - 1:
                        new_group.append(point)
                        points.remove(point)
                elif point[1] == element[1]:
                    if point[0] == element[0] + 1 or point[0] == element[0] - 1:
                        new_group.append(point)
                        points.remove(point)
        if len(new_group) == 0:
            groups.append(group)
            backtrack(points[:-1], [points[-1]])
        else:
            group.extend(new_group)
            backtrack(points, group)

    backtrack(points_list[:-1], [points_list[-1]])
    return groups


def plane(group):
    lines = defaultdict(list)
    columns = defaultdict(list)
    for element in group:
        lines[element[0]].append(element[1])
        columns[element[1]].append(element[0])
    return lines, columns


def perimeter(group):
    lines, columns = plane(group)
    return sum(calculate_perimeter(sorted(lines[key])) for key in lines.keys()) + sum(calculate_perimeter(sorted(columns[key])) for key in columns.keys())


def calculate_perimeter(axis):
    return sum(2 for index in range(len(axis) - 1) if axis[index] + 1 != axis[index + 1]) + 2


def side(group):
    lines, columns = plane(group)
    return calculate_side(lines) + calculate_side(columns)


def calculate_side(dictionary):
    edge_start, edge_end, results = set(), set(), 0
    for key in sorted(dictionary.keys()):
        new_edge_start = calculate_edge(sorted(dictionary[key]), 1)
        new_edge_end = calculate_edge(sorted(dictionary[key], reverse=True), - 1)
        if len(edge_start) == 0:
            results += len(new_edge_start) + len(new_edge_end)
        else:
            results += sum(1 for edge in new_edge_start if edge not in edge_start) + sum(1 for edge in new_edge_end if edge not in edge_end)
        edge_start, edge_end = new_edge_start, new_edge_end
    return results


def calculate_edge(axis, direction):
    edges = set([axis[index + 1] for index in range(len(axis) - 1) if axis[index] + direction != axis[index + 1]])
    edges.add(axis[0])
    return edges


if __name__ == '__main__':
    fileInput = open("input/Day12.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
