n = int(input())
size_list = list(map(int, input().split(" ")))
t, p = map(int, input().split(" "))

bundle = 0

for size_num in size_list:
    a, b = divmod(size_num, t)
    bundle += a if b == 0 else a + 1

print(bundle)

q, r = divmod(n, p)

print(q, r)
