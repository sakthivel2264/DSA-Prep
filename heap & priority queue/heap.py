

import heapq


A = [1, 6, 4,8,-3,-1,-8,0,13,10,5]

heapq.heapify(A)

print(A) #[-8, -3, -1, 0, 5, 1, 4, 8, 13, 10, 6]

# to find left & right in the array use 2i + 1 & 2i + 2

heapq.heappush(A, 2)

print(A)


minn = heapq.heappop(A)

print(A, minn)

heapq._heapify_max(A)

print(A)

# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)