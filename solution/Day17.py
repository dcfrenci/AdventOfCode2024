import re


def one(lines):
    numbers = [int(number) for number in re.findall(r"(\d+|-\d+)", lines)]
    register = {'a': numbers[0], 'b': numbers[1], 'c': numbers[2]}
    index = 0
    out = ""
    numbers = numbers[3:]
    while index < len(numbers) - 1:
        instruction = numbers[index]
        operand = get_operand(numbers[index + 1], register)
        index += 2
        if instruction == 0:
            register['a'] = int(register['a'] / pow(2, operand))
        elif instruction == 1:
            register['b'] = register['b'] ^ operand
        elif instruction == 2:
            # register['b'] = int((operand % 8) & 0b111)
            register['b'] = operand % 8
        elif instruction == 3:
            if register['a'] != 0:
                index = operand
        elif instruction == 4:
            register['b'] = register['b'] ^ register['c']
        elif instruction == 5:
            out = out + "".join(str(operand % 8) + ',')
        elif instruction == 6:
            register['b'] = int(register['a'] / pow(2, operand))
        elif instruction == 7:
            register['c'] = int(register['a'] / pow(2, operand))

    print("output:", out)
    print(out.replace(',', ''))


def get_operand(operand, register):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return register['a']
    if operand == 5:
        return register['b']
    if operand == 6:
        return register['c']
    return ValueError


if __name__ == '__main__':
    fileInput = open("input/Day17.txt", "r").read()
    one(fileInput)
    # two(fileInput.split("\n\n"))
