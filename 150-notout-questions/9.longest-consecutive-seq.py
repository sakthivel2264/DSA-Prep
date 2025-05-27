
# Longest Consecutive Sequence – Medium Level
# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Example 2
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

def longestConsecutive(arr):
    numSet = set(arr)
    longest = 0
    
    for num in numSet:
        if (num -1) not in numSet:
            length = 1
            
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
            
    return longest

nums = [2,20,4,10,3,4,5]

print(longestConsecutive(nums)) # 4