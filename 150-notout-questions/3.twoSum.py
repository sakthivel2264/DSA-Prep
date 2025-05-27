
# Example 1
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
# Example 3
# Input: nums = [5,5], target = 10
# Output: [0,1]

def twoSum(arr, target):
    hash = {}
    
    for i in range(len(arr)):
        if target - arr[i] in hash:
            return [hash[target-arr[i]], i]
            
        hash[arr[i]] = i
            
nums = [3,4,5,6]
target = 7

print(twoSum(nums, target)) # [0,1]