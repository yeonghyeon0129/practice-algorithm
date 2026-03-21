import sys

num = int(sys.stdin.readline())
data_dict = {}

for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    if x not in data_dict:
        data_dict[x] = []
    
    data_dict[x].append(y)

for x in sorted(data_dict.keys()):
    for y in sorted(data_dict[x]):
        sys.stdout.write(f"{x} {y}\n")
