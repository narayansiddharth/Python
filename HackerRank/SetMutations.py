def input_set_elements_count_limit_check(set_elements_count, limit=100):
    if not (set_elements_count > 0 & set_elements_count < limit):
        print("Total number of students in college not in range !!!")
        exit(-1)
    return set_elements_count


def input_set_elements(set_elements_count):
    elements = list(map(int, input().split()))
    elements = elements[0:set_elements_count]
    elements_set = set(elements)

    return elements_set


def command_executor(input_set, command, set_o):
    if command == "update":
        input_set.update(set_o)

    if command == "intersection_update":
        input_set.intersection_update(set_o)

    if command == "difference_update":
        input_set.difference_update(set_o)

    if command == "symmetric_difference_update":
        input_set.symmetric_difference_update(set_o)

    return input_set


if __name__ == '__main__':
    set_elements_count = int(input())
    input_set_elements_count_limit_check(set_elements_count, 1000)
    set_a = input_set_elements(set_elements_count)

    N = int(input())
    command_list = []
    outher_sets = []
    while (N > 0):
        command = input()
        args = str(command).split()
        command_list.append(args[0])
        input_set_elements_count_limit_check(int(args[1]))
        set_o = input_set_elements(int(args[1]))
        outher_sets.append(set_o)
        N -= 1

    index = 0
    for command in command_list:
        set_a = command_executor(set_a, command, outher_sets[index])
        index += 1

    sum = 0
    for elements in set_a:
        sum += elements

    print(sum)
