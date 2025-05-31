

def rotate(arr, k):
    n = len(arr)
    k = k % n # Handle k > n

    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(arr, k)) # Output: [5, 6, 7, 1, 2, 3, 4]