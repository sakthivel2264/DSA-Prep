
# Example 1
# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2
# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

def productOfArray(arr):
    res = [1] * len(arr)
    prefix = 1
    
    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]
    
    postfix = 1
    for i in range(len(arr)-1,-1,-1):
        res[i] *= postfix
        postfix *= arr[i]

    return res    

nums = [1,2,4,6]
print(productOfArray(nums))   