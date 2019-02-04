if __name__ == '__main__':
    n = int(input())
    integer_map = map(int, input().split())
    print(integer_map)

    temp = ""
    for t in integer_map:
        if temp == "":
            temp = str(t)
        else:
            temp = temp + ", " + str(t)

    print(abs(hash(temp)))
