# Python List Operations

List_1 = [1, 2, 3, 4]
List_2 = [5, 6, 7, 8, 9]
List_3 = ["Hello"]
List = List_1 + List_2

print("Length of List is ", len(List))
print("Accessing List Operation : ", List[1])
print("List Concatenated : ", List)
print("List Repetitions :", List_3 * 3)

List.append(9)

print(List)

List.sort()
print(List)

List.remove(9)
print(List)
