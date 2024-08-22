from collections import Counter
def min_distinct_elements_to_remove(arr):
    # Step 1: Count the frequency of each element
    frequency = Counter(arr)

    # Step 2: Sort elements by their frequency in descending order
    sorted_frequencies = sorted(frequency.values(), reverse=True)

    # Step 3: Calculate the original size and target size
    original_size = len(arr)
    target_size = original_size // 2

    # Initialize variables to track removal process
    removed_size = 0
    distinct_elements_removed = 0

    # Remove elements with the highest frequency first
    for freq in sorted_frequencies:
        removed_size += freq
        distinct_elements_removed += 1
        if original_size - removed_size <= target_size:
            break

    return distinct_elements_removed

# Read input values
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the result
result = min_distinct_elements_to_remove(arr)
print(result)
