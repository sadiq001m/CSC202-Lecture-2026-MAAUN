import random

# 1️⃣ Generate Data
scores = [random.randint(50, 100) for _ in range(10)]
print("Original Scores:", scores)


# 2️⃣ Recursive Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# Sort scores
sorted_scores = merge_sort(scores)
print("Sorted Scores:", sorted_scores)


# 3️⃣ Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 4️⃣ User Input
target_score = int(input("Enter the score to search: "))

index = binary_search(sorted_scores, target_score)

if index != -1:
    print(f"Candidate with score {target_score} found at rank {index}.")
else:
    print("Score not found.")