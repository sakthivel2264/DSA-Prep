arr = [2,5,8,1,4,9,3,7]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left)+ middle + quick_sort(right)

print(quick_sort(arr))

#TimeComplexity = O(n log n) average, O(n²) worst-case

# [expression for item in iterable if condition]
# expression → The value to be added to the list.
# item → Each element in the iterable (like a list or range).
# iterable → The collection we are iterating over (e.g., arr).
# condition (optional) → A filter that decides which elements to include.


# Python’s built-in sorted() uses Timsort (a hybrid of Merge + Insertion Sort) — stable and fast.