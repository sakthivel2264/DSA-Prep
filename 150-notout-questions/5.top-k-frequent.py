
# Example 1
# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2
# Input: nums = [7,7], k = 1

# Output: [7]

from collections import Counter

def top_k(arr, k):
    count = Counter(arr)  # Dictionary of element: frequency
    most_common = count.most_common(k)  # Returns list of tuples (element, frequency)
    print(most_common)
    return [item for item, freq in most_common]


nums = [1,2,2,3,3,3,3]
k = 2

print(top_k(nums, k))