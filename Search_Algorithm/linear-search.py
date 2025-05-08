arr = [1,2,3,4,5,6,7,8,9]
find = 7

for i in range(len(arr)):
    if arr[i] == find:
        print(f"The Index:",i,"The value:", arr[i])
        break

#Time Complexity = O(n)