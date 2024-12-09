

def one(lines):
    number_block = []
    dot_block = []
    for line in lines:
        number = True
        value = 0
        for letter in list(line):
            if number:
                number_block.append([str(value) for i in range(int(letter))])
                value += 1
                number = False
            else:
                dot_block.append(list('.' * int(letter)))
                number = True
    string = []
    for start in range(len(number_block)):
        if start >= len(number_block):
            break
        string.extend(number_block[start])
        for dot in range(len(dot_block[start])):
            if start == len(number_block) - 1:
                break
            string.append(number_block[-1][-1])
            number_block[-1] = number_block[-1][:-1]
            if len(number_block[-1]) <= 0:
                number_block = number_block[:-1]
    results = 0
    for index in range(len(list(string))):
        results += index * int(string[index])
    print(results)


def two(lines):
    string, value = [], 0
    for line in lines:
        for index, char in enumerate(line):
            if index % 2 == 0:
                string.append([str(value) for time in range(int(char))])
                value += 1
            else:
                string.append(list('.' * int(char)))
    while any('.' in sub for sub in string):
        for start in range(1, len(string), 2):
            insert = False
            if start >= len(string):
                break
            if '.' in string[start]:
                for slide in range(0, len(string), 2):
                    if start >= len(string) - slide - 1:
                        string[start] = ['0' if x == '.' else x for x in string[start]]
                        break
                    if string[start].count('.') >= len(string[- 1 - slide]) > 0 and string[- 1 - slide].count(':') != len(string[- 1 - slide]):
                        index = string[start].index('.')
                        string[start], string[- 1 - slide] = string[start][:index] + string[- 1 - slide] + string[start][index + len(string[- 1 - slide]):], list(':' * len(string[- 1 - slide]))
                        insert = True
                        break
            if insert:
                break
    results, index = 0, 0
    for block in string:
        for char in block:
            if char != ':':
                results += index * int(char)
            index += 1
    print(results)


if __name__ == '__main__':
    fileInput = open("input/Day9.txt", "r").read()
    # one(fileInput.split("\n"))
    two(fileInput.split("\n"))
