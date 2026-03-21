import sys

sorted_dict = {i : [] for i in range(1, 51)}

num = int(sys.stdin.readline())

for i in range(num):
    text = str(sys.stdin.readline())
    length = len(text) - 1
    sorted_dict[length].append(text)

for values in sorted_dict.values():
    values = list(set(values))
    for value in sorted(values):
        sys.stdout.write(value)
