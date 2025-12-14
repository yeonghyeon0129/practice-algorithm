count = int(input())

num_list = list(map(int, input().split(' ')))
cnt = 0
p = (2, 3, 5, 7)
r = (4, 6, 8, 9)
for num in num_list:
    if num < 2 or num in r:
        continue

    if num in p:
        cnt += 1
        continue

    val = int(num ** 0.5)
    prime = True
    for i in range(2, val + 1):
        if num % i == 0:
            prime = False
    if prime:
        cnt += 1

print(cnt)
        