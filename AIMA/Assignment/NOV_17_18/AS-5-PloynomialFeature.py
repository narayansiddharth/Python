def PolynomialFeature(items):
    finallist = []
    if len(items) == 0:
        print("Empty list")
    elif len(items[0]) == 2:
        for row in items:
            newlist = []
            newlist.append(1 * 1.0)
            newlist.append(row[0] * 1.0)
            newlist.append(row[1] * 1.0)
            newlist.append(row[0] * row[0] * 1.0)
            newlist.append(row[0] * row[1] * 1.0)
            newlist.append(row[1] * row[1] * 1.0)
            finallist.append(newlist)
    elif len(items[0]) == 3:
        for row in items:
            newlist = []
            newlist.append(1 * 1.0)
            newlist.append(row[0] * 1.0)
            newlist.append(row[1] * 1.0)
            newlist.append(row[2] * 1.0)
            newlist.append(row[0] * row[1] * 1.0)
            newlist.append(row[0] * row[2] * 1.0)
            newlist.append(row[1] * row[2] * 1.0)
            newlist.append(row[0] * row[1] * row[2] * 1.0)
            finallist.append(newlist)
    return finallist


items = [[0, 1], [2, 3], [4, 5]]
print(items)
print(PolynomialFeature(items))
items = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(PolynomialFeature(items))
