
# Example 1
# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2
# Input: nums = [1, 2, 3, 4]
# Output: false

def dup_int(arr):
    seen = set()
    
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        else:
            seen.add(arr[i])
            
    return False

A = [1,2,3,3] # True
print(dup_int(A))
