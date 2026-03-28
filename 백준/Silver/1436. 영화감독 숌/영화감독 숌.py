import sys

count = int(sys.stdin.readline())
n = 0
title = 666

while n < count:
    if "666" in str(title):
        n += 1
    title += 1

print(title -1)