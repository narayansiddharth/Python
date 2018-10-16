# Listing 1-10. Example code for bitwise operators
# Basic six bitwise operations # Let x = 10 (in binary0000 1010) and y = 4 (in binary0000 0100)
x: int = 10
y: int = 4
print("x = ", x)
print("y = ", y)

print("x >> y : ", x >> y)  # Right Shift
print("x << y : ", x << y)  # Left Shift
print("x & y : ", x & y)  # Bitwise AND
print("x | y : ", x | y)  # Bitwise OR
print("x ^ y : ", x ^ y)  # Bitwise XOR
print("~x : ", ~x)  # Bitwise NOT
