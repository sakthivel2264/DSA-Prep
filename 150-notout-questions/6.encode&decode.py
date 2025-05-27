
# Example 1
# Input: ["this","course","are","best"]

# Output: ["this","course","are","best"]
# Example 2
# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

class Codec:
    # Encodes a list of strings to a single string
    def encode(self, strs):
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    # Decodes a single string to a list of strings
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            # Find the separator #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Get length of next string
            j += 1  # Move past '#'
            word = s[j:j + length]  # Extract word
            res.append(word)
            i = j + length  # Move to next encoded word
        return res
    
codec = Codec()

# Example 1
input1 = ["this", "course", "are", "best"]
encoded1 = codec.encode(input1)
decoded1 = codec.decode(encoded1)
print("Encoded:", encoded1)
print("Decoded:", decoded1)

# Example 2
input2 = ["we", "say", ":", "yes"]
encoded2 = codec.encode(input2)
decoded2 = codec.decode(encoded2)
print("Encoded:", encoded2)
print("Decoded:", decoded2)

