num = int(input())

for n in range(num):
    for i in range(n+1):
        print("*") if i == n else print("*", end = "")