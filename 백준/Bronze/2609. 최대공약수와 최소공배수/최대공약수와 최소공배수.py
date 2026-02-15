f, s = map(int, input().split())

a, b = f, s

while b != 0:
    a, b = b, a % b

gcd = a
lcm = f * s // gcd

print(gcd)
print(lcm)