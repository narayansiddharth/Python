def input_limit_check(group_count, limit=1000):
    if not (group_count > 0 & group_count < limit):
        print("Total number of students in college not in range !!!")
        exit(-1)
    return group_count


if __name__ == "__main__":
    group_count = int(input())
    input_limit_check(group_count)
    room_list = list(map(int, input().split()))
    room_set = set(room_list)

    print(((sum(room_set) * group_count) - (sum(room_list))) // (group_count - 1))
