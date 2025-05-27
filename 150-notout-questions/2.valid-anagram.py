
# Example 1
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2
# Input: s = "jar", t = "jam"
# Output: false

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


s = "racecar"
t = "carrace"

print(valid_anagram(s,t)) # True