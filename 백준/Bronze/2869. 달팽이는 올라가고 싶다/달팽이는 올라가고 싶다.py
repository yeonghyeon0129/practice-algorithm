up, down, v = map(int, input().split(' '))

m, n = divmod(v - down, up-down)
if n > 0:
    m += 1

print(m)