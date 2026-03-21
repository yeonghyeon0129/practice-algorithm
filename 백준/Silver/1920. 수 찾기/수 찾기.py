import sys

num = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split(' ')))
num = int(sys.stdin.readline())
for m in list(map(int, sys.stdin.readline().split(' '))):
    if m in n_set:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
