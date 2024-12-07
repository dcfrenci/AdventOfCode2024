from itertools import product


def one(lines):
    results = 0
    for line in lines:
        test_value = int(line.split(':')[0])
        numbers = [int(number) for number in line.split(':')[1].split()]
        for string in product(['+', '*'], repeat=len(numbers) - 1):
            if test_value == calculate(string, numbers):
                results += test_value
                break
    print(results)


def calculate(string, numbers):
    results = numbers[0]
    for index in range(len(numbers) - 1):
        if string[index] == '+':
            results += numbers[index + 1]
        else:
            results *= numbers[index + 1]
    return results


def two(lines):
    results = 0
    for line in lines:
        test_value = int(line.split(':')[0])
        numbers = [int(number) for number in line.split(':')[1].split()]
        equation = False
        for string in product(['+', '*'], repeat=len(numbers) - 1):
            if test_value == calculate(string, numbers):
                results += test_value
                equation = True
                break
        if not equation:
            for concatenate in combine(numbers, 0):
                for string in product(['+', '*'], repeat=len(concatenate) - 1):
                    if test_value == calculate(string, concatenate):
                        results += test_value
                        break
    print(results)


def combine(numbers, original):
    combination = []
    for i in range(original, len(numbers) - 1):
        # ([numbers[0]] if i == 1 else []) +
        new_combination = (numbers[:i] if len(numbers[:i]) > 0 else []) + [numbers[i] * pow(10, len(str(numbers[i + 1]))) + numbers[i + 1]] + (numbers[i + 2:] if len(numbers[i + 2:]) > 0 else [])
        combination.append(new_combination)
        combination.extend(combine(numbers, original + 1))
    if original == 0:
        test = 0
    return combination


if __name__ == '__main__':
    fileInput = open("input/Day7.txt", "r").read()
    # one(fileInput.split("\n"))
    two(fileInput.split("\n"))
