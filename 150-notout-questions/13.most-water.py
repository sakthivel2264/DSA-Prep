
# Container with Most Water – Hard Level Problem
# You are given an array heights, where each element heights[i] represents the height of a vertical bar at position i. Your task is to select any two bars to form a container, with the width of the container being the distance between the two bars.

# The goal is to find the maximum amount of water that this container can hold. Return the largest possible value of water that can be stored.

# Example 1
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36
# Example 2
# Input: height = [2,2,2]
# Output: 4

def mostWater(nums):
    l = 0
    r = len(nums) - 1
    max_area = 0
    
    while l < r:
        area = (r - l) * min(nums[l], nums[r])
        max_area = max(max_area, area)
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
        
    return max_area

height = [1,7,2,5,4,7,3,6]
print(mostWater(height)) # 36