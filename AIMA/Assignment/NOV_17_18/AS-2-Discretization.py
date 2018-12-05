# Write code in Python for Discretization without using any library

from typing import List, Any, Union


def discretization(items: object, interval: object) -> object:
    stepsize: float = len(items) / interval
    items.sort()
    arr: List[Union[float, Any]] = []
    for i in range(0, interval):
        j = float(i * stepsize) + 1
        arr.append(j)
    arr.append(items[-1] + (items[-1] - items[0]) * 0.001)
    # print(arr)
    return arr


def printDiscretizedvalues(items, interval):
    interval = (interval * 1.0)
    intervalType = type(interval)
    stringArrwithcomma = ""
    stringArrwithlessthan = ""
    index = 0
    while index < len(items):
        if index == len(items) - 1:
            stringArrwithcomma += ("[" + str(items[index - 1]) + ", " + str(items[index]) + ")")
            stringArrwithlessthan += "[" + str(items[index - 1]) + ", " + str(items[index]) + ")"
        else:
            stringArrwithcomma += "[" + str(items[index]) + ", " + str(items[index + 1]) + "),"
            stringArrwithlessthan += "[" + str(items[index - 1]) + ", " + str(items[index]) + ") < "
        index += 1

    print("([" + stringArrwithcomma + "]")
    print(" Categories (" + str(int(interval)) + "  " + str(intervalType) + ")")
    print("[" + stringArrwithlessthan + "]")
    print("array({0}))".format(items))


items = [1, 3, 2, 7, 5]
interval: int = 4
discretizedValues = discretization(items, interval)
printDiscretizedvalues(discretizedValues, interval)
