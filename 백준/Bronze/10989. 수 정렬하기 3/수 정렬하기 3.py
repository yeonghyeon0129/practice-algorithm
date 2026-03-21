import sys

def proc_large_data(num):
    counter = [0] * 10001

    for i in range(num):
        n = int(sys.stdin.readline())
        counter[n] += 1

    for k, v in enumerate(counter):
        for _ in range(v):
            yield k

def proc_small_data(num):
    result_list = []
    for i in range(num):
        n = int(sys.stdin.readline())
        result_list.append(n)
    
    result = sorted(result_list)
    return result

num = int(sys.stdin.readline())
result = None

if num > 10000:
    result = proc_large_data(num)
else:
    result = proc_small_data(num)

for r in result:
    sys.stdout.write(str(r) + '\n')

