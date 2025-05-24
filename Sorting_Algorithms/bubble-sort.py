arr = [5, 8, 3, 6, 9, 1, 2, 8]

for i in range(len(arr)): #N Times
    for j in range(len(arr)- i - 1): #N - 1 Times
        print(arr[j], arr[j+1])
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            

print(arr)

# timeComplexity = O(N^2)
