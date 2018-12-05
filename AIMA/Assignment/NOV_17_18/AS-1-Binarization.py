# Write code in Python for Binarization without using any library
from typing import List


def Binarization(inputlist, symbol: object, threshold: object) -> object:
    finalList: object = []
    for row in inputlist:
        innerList: object = []
        for col in row:
            if symbol == '>':
                if col >= threshold:
                    innerList.append(1)
                else:
                    innerList.append(0)
            else:
                if threshold > col:
                    innerList.append(1)
                else:
                    innerList.append(0)
        finalList.append(innerList)
    return finalList


def inputList(row, col):
    inputlist: List[List[int]] = []
    for i in range(row):
        list = []
        print('enter {0} list elements, please press enter after each element :'.format(col))
        for j in range(col):
            list.append(int(input().strip()))
        inputlist.append(list)
    return inputlist


row = int(input("enter no of rows: "))
col = int(input("enter no of coloumns: "))
inputlist = inputList(row, col)

# [int(i) for i in list(input().split())]
threshold = int(input("Enter the threshold value :"))
key = input(
    "Do you want set 1 for value which are greter than equal threshold , then press 'y'; if you want set 0 press any "
    "key...")

print("Input List :: ", inputlist)
print("Threshold Value : ", threshold)
if key == 'y':
    output = Binarization(inputlist, '>', threshold)
else:
    output = Binarization(inputlist, '<', threshold)

print(output)
