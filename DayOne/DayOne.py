#Parse Input

left, right = [],[]
f = open("input.txt", "r")
for i in f.readlines():
    item = i.split('   ')
    left.append(int(item[0]))
    right.append(int(item[1].replace("\n","")))

#Part 1

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total_distance

total_distance = calculate_total_distance(left, right)
print(f"Total distance: {total_distance}")


#Part 2

from collections import Counter

def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    similarity_score = sum(left * right_counts[left] for left in left_list)

    return similarity_score

similarity_score = calculate_similarity_score(left, right)
print(f"Similarity score: {similarity_score}")

