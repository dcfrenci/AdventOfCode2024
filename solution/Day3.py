
def one(line):
    results = 0
    for char in range(len(line)):
        if char + len("mul(") <= len(line) and line[char: char + len("mul(")] == "mul(" and line[char:].find(')') != -1:
            nums = line[char + len("mul("): char + line[char:].find(')')].split(',')
            if len(nums) == 2:
                correct = True
                for num in nums:
                    if len(num) == 0:
                        correct = False
                        break
                    for subs in num:
                        if not subs.isdigit():
                            correct = False
                            break
                if correct:
                    results += int(nums[0]) * int(nums[1])
    print(results)


def two(line):
    do = 0
    dont = 0
    results = 0
    for char in range(len(line)):
        if char + len("do()") <= len(line) and line[char: char + len("do()")] == "do()":
            do = char
        if char + len("don't()") <= len(line) and line[char: char + len("don't()")] == "don't()":
            dont = char
        if char + len("mul(") <= len(line) and line[char: char + len("mul(")] == "mul(" and line[char:].find(')') != -1:
            nums = line[char + len("mul("): char + line[char:].find(')')].split(',')
            if len(nums) == 2:
                correct = True
                for num in nums:
                    if len(num) == 0:
                        correct = False
                        break
                    for subs in num:
                        if not subs.isdigit():
                            correct = False
                            break
                if correct and do >= dont:
                    results += int(nums[0]) * int(nums[1])
    print(results)


if __name__ == '__main__':
    fileInput = open("input/Day3.txt", "r").read()
    one(fileInput)
    two(fileInput)