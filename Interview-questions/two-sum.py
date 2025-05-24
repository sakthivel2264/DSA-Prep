# Two Sum
# Problem: Given an array, find two numbers that add up to a target.

# Concepts: Hash maps, arrays.


def twoSum(nums, target):
    
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target -num ], i]
        seen[num] = i


# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]