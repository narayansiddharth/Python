# Listing 1-23. Example code for deleting a list element
from typing import List, Union

list_1: List[Union[str, int]] = ['c', 'b', 2015, 3, 2, 1, 2019]
print("list_1 values: ", list_1)
# Deleting list element
del list_1[5];
print("After deleting value at index 2 : ", list_1)
