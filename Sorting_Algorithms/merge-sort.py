arr = [2,5,8,1,4,9,3,7]

def merge(a, b):
    c = []
    i = 0 
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1

    return c

def merge_sort(a):
    if len(a) == 1:
        return a
    
    return merge(merge_sort(a[:int(len(a)/2)]), merge_sort(a[int(len(a)/2):]))

print(merge_sort(arr))

# TimeComplexity = O(NlogN)