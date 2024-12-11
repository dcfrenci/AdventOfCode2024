import timeit
from collections import defaultdict


def one(lines):
    stones_map = defaultdict(int)
    for stone in [int(number) for line in lines for number in line.split()]:
        stones_map[int(stone)] += 1
    for time in range(25):
        stones_map = blink(stones_map)
    print(sum(stones_map.values()))


def two(lines):
    stones_map = defaultdict(int)
    for stone in [int(number) for line in lines for number in line.split()]:
        stones_map[int(stone)] += 1
    for time in range(75):
        stones_map = blink(stones_map)
    print(sum(stones_map.values()))


def blink(stones_map):
    new_stones_map = defaultdict(int)
    for stone, count in stones_map.items():
        new_stones = transform(stone)
        for new_stone in new_stones:
            new_stones_map[new_stone] += count
    return new_stones_map


def transform(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return [int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])]
    else:
        return [stone * 2024]


if __name__ == '__main__':
    fileInput = open("input/Day11.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
    execution_time = timeit.timeit(lambda: one(fileInput.split("\n")), number=1)
    print(f"Execution time: {execution_time:.6f} second")
    execution_time = timeit.timeit(lambda: two(fileInput.split("\n")), number=1)
    print(f"Execution time: {execution_time:.6f} second")
