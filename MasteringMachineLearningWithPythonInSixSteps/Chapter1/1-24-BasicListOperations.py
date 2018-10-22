# Listing 1-24. Example code for basic operations on lists
from typing import List, Union

list_1 = ['Statistics', 'Programming', 2015, 2017, 2018, 'a', 'b', 1, 2, 3, 4, 5, 6, 7]
list_2 = ['a', 'b', 1, 2, 3, 4, 5, 6, 7]
print("Length: ", len(list_1))
print("Concatenation: ", [1, 2, 3] + [4, 5, 6])
print("Repetition :", ['Hello'] * 4)
print("Membership :", 3 in [1, 2, 3])
print("Iteration :")
for x in [1, 2, 3]:
    print(x)
# Negative sign will count from the right
print("slicing :", list_1[-2])
# If you dont specify the end explicitly, all elements from the specified start index will be printed
print("slicing range: ", list_1[1:])
# Comparing elements of lists
# print("Compare two lists: ", cmp(list([1, 2, 3, 4]), list([1, 2, 3])))
print("Max of list: ", max([1, 2, 3, 4, 5]))
print("Min of list: ", min([1, 2, 3, 4, 5]))
print("Count number of 1 in list: ", [1, 1, 2, 3, 4, 5, ].count(1))
list_1.extend(list_2)
print("Extended :", list_1)
print("Index for Programming : ", list_1.index('Programming'))
print(list_1)
print("pop last item in list: ", list_1.pop())
print("pop the item with index 2: ", list_1.pop(2))
list_1.remove('b')
print("removed b from list: ", list_1)
list_1.reverse()
print("Reverse: ", list_1)
list_1: List[Union[str, int]] = ['a', 'b', 'c', 1, 2, 3]
list_1.sort()
print("Sort ascending: ", list_1)
list_1.sort(reverse=True)
print("Sort descending: ", list_1)
