# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

input_string, k = (x for x in input().split(' '))
k = int(k)
input_string = list(input_string)
input_string.sort()
for chars in combinations_with_replacement(input_string, k):
    print(''.join(chars))
