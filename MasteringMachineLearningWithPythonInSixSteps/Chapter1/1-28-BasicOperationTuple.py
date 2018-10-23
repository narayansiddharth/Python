# Listing 1-28. Example code for basic operations on tupe (not exhaustive)
# Basic Tuple operations

Tuple = ('a', 'b', 'c', 'd', 1, 2, 3)
print("Length of Tuple: ", len(Tuple))
Tuple_Concat = Tuple + (7, 8, 9)
print("Concatenated Tuple: ", Tuple_Concat)

print("Repetition: ", (1, 'a', 2, 'b') * 3)
print("Membership check: ", 3 in (1, 2, 3))
# Iteration
for x in (1, 2, 3):
    print(x)
print("Negative sign will retrieve item from right: ", Tuple_Concat[-2])
print("Sliced Tuple [2:] ", Tuple_Concat[2:])
# Comparing two tuples
print("Comparing tuples (1,2,3) and (1,2,3,4): ", (1, 2, 3) >= (1, 2, 3, 4))
print("Comparing tuples (1,2,3,4) and (1,2,3): ", (1, 2, 3, 4) >= (1, 2, 3))
# Find max
print("Max of the Tuple (1,2,3,4,5,6,7,8,9,10): ", max((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print("Min of the Tuple (1,2,3,4,5,6,7,8,9,10): ", min((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print("List [1,2,3,4] converted to tuple: ", type(tuple([1, 2, 3, 4])))
