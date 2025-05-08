arr = [2,5,8,1,4,9]

for i in range(len(arr)): #N times
    min_index = i
    for j in range(i, len(arr)): #N-i Times
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

# timeComplexity = O(N^2)