import re

#Parse Input

with open("Day 3/input.txt", "r") as f:
    corrupted = f.read()

#Part 1

total = 0
for mul in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', corrupted):
    total += (int(mul[0])*int(mul[1]))
print(total)

#Part 2

def calculate_enabled_mul_sum(memory_string):
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    
    mul_enabled = True
    total_sum = 0

    tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory_string)

    for token in tokens:
        if mul_pattern.match(token):
            if mul_enabled:
                a, b = map(int, mul_pattern.match(token).groups())
                total_sum += a * b
        elif do_pattern.match(token):
            mul_enabled = True
        elif dont_pattern.match(token):
            mul_enabled = False

    return total_sum


result = calculate_enabled_mul_sum(corrupted)
print(result)


    
    