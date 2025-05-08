def binary_search(arr, target):
    left= 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow

        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:  
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found


arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)
print("Element found at index:", result)

#Time Complexity = O(log n)