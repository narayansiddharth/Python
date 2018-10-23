# Listing 1-13. Example code for identity operators
from typing import List

var1: int = 5
var1 = 5

var2: str = 'Hello'
var2 = 'Hello'

var3: List[int] = [1, 2, 3]
var3 = [1, 2, 3]

print(var1 is not var1)
print(var2 is var2)
print(var3 is var3)
