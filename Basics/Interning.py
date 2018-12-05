'''
Python will also allocate the same memory address in the following two scenarios.

The strings don’t have whitespaces and contain less than 20 characters.
In case of Integers ranging between -5 to +255.
This concept is known as Interning. Python does it to save memory.
'''

test1 = "Learn Python"
value1 = id(test1)
print(value1)
test2 = "Learn Python"
value2 = id(test2)
print(value2)
