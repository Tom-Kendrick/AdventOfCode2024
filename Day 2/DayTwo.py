#Parsing Input

with open("DayTwo/input.txt", "r") as f:
    levels = [[int(num.strip()) for num in i.split(' ')] for i in f.readlines()]


#Part 1

safe = 0
for report in levels:
    if sorted(report) == report or sorted(report, reverse=True) == report:
        if all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)):
            safe += 1
print(safe)

#Part 2

safe = 0
def is_safe(report):
    return (sorted(report) == report or sorted(report, reverse=True) == report) and \
           all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

for report in levels:
    if is_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe += 1
                break
print(safe)
