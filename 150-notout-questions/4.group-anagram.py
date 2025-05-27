
# Example 1
# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2
# Input: strs = ["x"]

# Output: [["x"]]
# Example 3
# Input: strs = [""]

# Output: [[""]]

def groupAnagram(arr):
    
    hashMap = {}
    
    for word in arr:
        
        key = tuple(sorted(word))
        
        if key in hashMap:
            hashMap[key].append(word)
        else:
            hashMap[key] = [word]
            
    return list(hashMap.values())

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(groupAnagram(strs))
# Output: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
