import sys
import math

count = int(sys.stdin.readline())
if count == 1:
    print(1)
else:
    n = int(math.log2(count))
    r = count - 2 ** n
    if r == 0:
        print(count)
    else:
        print(2 * r)
