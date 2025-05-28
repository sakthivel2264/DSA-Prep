
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