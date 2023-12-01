import re

def main():
    input = read_input()

    part_one_result = part_one(input)
    part_two_result = part_two(input)
    
    output_results(part_one_result, part_two_result)

def part_one(input):
    value = 0
    for x in input:
        y = re.sub(r'[a-z]', '', x.lower())

        z = int(f"{y[0]}{y[-1]}")
        value = value + z

    return value

def part_two(input):
    value = 0
    strings = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'} # GENIUS LOL
    for x in input:
        for key in strings:
            x = x.replace(key, strings[key])

        y = re.sub(r'[a-z]', '', x.lower())

        z = int(f"{y[0]}{y[-1]}")
        value = value + z

    return value

def output_results(part_one_result, part_two_result):
    print(f'PART ONE: {part_one_result}')
    print(f'PART TWO: {part_two_result}')

def read_input():
    with open('Day 1/input.txt', 'r') as file:
        text_array = [line.strip() for line in file.readlines()]

    return text_array

if __name__ == '__main__':
    main()