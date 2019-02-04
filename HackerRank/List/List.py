"""

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

"""


def print_commands():
    print("Available Commands :")
    print("insert i e: Insert integer e at position i.")
    print("Print the list.")
    print("remove e: Delete the first occurrence of integer e.")
    print("append e: Insert integer e at the end of the list.")
    print("sort: Sort the list.")
    print("pop: Pop the last element from the list.")
    print("reverse: Reverse the list.")


def command_executor(int_list, command):
    # Spilt Command by spaces
    args = str(command).split()

    if args[0] == "print":
        print(int_list)

    if args[0] == "insert":
        int_list.insert(int(args[1]), int(args[2]))
    if args[0] == "append":
        int_list.append(int(args[1]))

    if args[0] == "sort":
        int_list = int_list.sort()
    if args[0] == "reverse":
        int_list = int_list.reverse()

    if args[0] == "remove":
        int_list.remove(int(args[1]))
    if args[0] == "pop":
        int_list.pop(len(int_list) - 1)

    return int_list


if __name__ == '__main__':
    print_commands()
    N = int(input())
    command_list = []

    int_list = []

    while (N > 0):
        command_list.append(input())
        N -= 1

    for command in command_list:
        command_executor(int_list, command)
