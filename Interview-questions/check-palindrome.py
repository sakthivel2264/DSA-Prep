# Check Palindrome
# Problem: Check if a string is a palindrome.

# Concepts: String comparison.

def palindrome(string):
    
    return string == string[::-1]

# Example usage
string = "racecar"
result = palindrome(string)
print(result)  # Output: True