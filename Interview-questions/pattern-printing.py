
# 1. Left-Aligned Right-Angled Triangle

n = 5
print("1. Left-Aligned Right-Angled Triangle")
for i in range(1, n + 1):
    print("* " * i)
    
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# 2. Right-Aligned Right-Angled Triangle

n = 5
print("2. Right-Aligned Right-Angled Triangle")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)
    
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# 3. Pyramid Pattern

n = 5
print("3. Pyramid Pattern")
for i in range(1, n + 1):
    print(" " * (n-i) + "* " * i)
    
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 


# 4. Inverted Right-Angled Triangle

n = 5
print("4. Inverted Right-Angled Triangle")
for i in range(n, 0, -1):
    print("* " * i)
    
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


# 5. Inverted Pyramid Pattern

n = 5 
print("5. Inverted Pyramid Pattern")
for i in range (n, 0 , -1):
    print(" " * (n-i) + "* " * i)
    

# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


# 6. Number Pyramid

n = 5

print("6. Number Pyramid")
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 


#  7. Floyd’s Triangle

n = 5
num = 1

print(" 7. Floyd’s Triangle")
for i in range(1, n):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
    
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

    
#  8. Binary Triangle

n = 5
print("8. Binary Triangle")
for i in range(1, n):
    for j in range(1, i + 1):
        print((j + i)% 2, end=" ")
    print()    
    
# 0
# 1 0
# 0 1 0
# 1 0 1 0


# 9. Diamond Pattern

n = 5
print("9. Diamond Pattern")
for i in range(1, n+1):
    print(" " * (n-i), "* " * i)
for i in range(n -1, 0, -1):
    print(" "* (n-i), "* " * i)


#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


# 10. Pascal’s Triangle

n = 5
print("10. Pascal’s Triangle")
for i in range(n):
    print(' ' * (n - i), end='')
    val = 1
    for j in range(i+ 1):
        print(val, end=" ")
        val = val * (i-j)//(j +1)
    print()
    
#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 

# 11. Alphabet Pattern

n = 5
print("11. Alphabet Pattern")
for i in range(n):
    print((chr(65 + i) + " ")* (i + 1))
    
# A
# B B
# C C C
# D D D D
# E E E E E