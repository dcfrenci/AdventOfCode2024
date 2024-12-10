def one(lines):
    print(sum(int(line.split(':')[0]) for line in lines
              if int(line.split(':')[0]) in combination([int(number) for number in line.split(':')[1].split()], set(), False)))


def two(lines):
    print(sum(int(line.split(':')[0]) for line in lines
              if int(line.split(':')[0]) in combination([int(number) for number in line.split(':')[1].split()], set(), True)))


def combination(array, results, concatenation):
    def combine(numbers, index, value):
        if index + 1 >= len(numbers):
            return results.add(value)
        combine(numbers, index + 1, value * numbers[index + 1])
        combine(numbers, index + 1, value + numbers[index + 1])
        if concatenation:
            combine(numbers, index + 1, int(str(value) + str(numbers[index + 1])))

    combine(array, 0, array[0])
    return results


if __name__ == '__main__':
    fileInput = open("input/Day7.txt", "r").read()
    one(fileInput.split("\n"))
    two(fileInput.split("\n"))
