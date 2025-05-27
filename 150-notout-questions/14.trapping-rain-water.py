
# Trapping Rain Water Leetcode Problem :
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example :
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trap(height):
    l = 0
    r = len(height) - 1
    trapped = 0
    left_max, right_max = 0, 0
    
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                trapped += left_max - height[l]
            l += 1
            
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                trapped += right_max - height[r]
            r -= 1
            
    return trapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))