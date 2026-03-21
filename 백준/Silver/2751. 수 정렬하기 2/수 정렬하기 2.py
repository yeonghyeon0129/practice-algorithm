import sys

num = int(sys.stdin.readline())

result_list = []

for i in range(num):
    n = int(sys.stdin.readline())
    result_list.append(n)

sorted_list = sorted(result_list)

for result in sorted_list:
    sys.stdout.write(f"{result}\n")
