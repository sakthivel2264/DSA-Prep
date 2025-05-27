
# Program to check Valid Palindrome – Medium Level(Using Two Pointer)
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have “wasitacaroracatisaw”, which is a palindrome.

# Example 2
# Input: s = "tab a cat"
# Output: false
# Explanation: “tabacat” is not a palindrome.


import re


def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True
        
sen = "Was it a car or a cat I saw?"
print(isPalindrome(sen)) # True
