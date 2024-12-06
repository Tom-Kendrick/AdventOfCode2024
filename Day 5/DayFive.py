# Parse input

with open("Day 5/input.txt", "r") as f:
    inp = f.readlines()

inp = [line.strip() for line in inp]
rules_list, updates_list = inp[:inp.index('')], inp[inp.index('')+1:]

# Part 1

rules, updates = [], []
for rule in rules_list:
    X, Y = map(int, rule.split('|'))
    rules.append((X, Y))
for update in updates_list:
    updates.append(list(map(int, update.split(','))))


def is_valid_update(update, rules):
    update_set = set(update)
    
    for X, Y in rules:
        if X in update_set and Y in update_set:
            if update.index(X) > update.index(Y):
                return False
    return True

def get_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]


valid_updates = []
middle_sum = 0

for update in updates:
    if is_valid_update(update, rules):
        valid_updates.append(update)
        middle_sum += get_middle_page(update)

print(middle_sum)


# Part 2

from collections import defaultdict, deque

def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for X, Y in rules:
        if X in pages and Y in pages:
            graph[X].append(Y)
            in_degree[Y] += 1
    
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

incorrect_updates = []
middle_sum = 0

for update in updates:
    if not is_valid_update(update, rules):
        incorrect_updates.append(update)

for update in incorrect_updates:
    corrected_order = topological_sort(update, rules)

    middle_page = get_middle_page(corrected_order)
    middle_sum += middle_page

print(middle_sum)
