import sys

num = int(sys.stdin.readline())

result = {}

for n in range(num):
    age, name = sys.stdin.readline().split(' ')
    age = int(age)
    if age not in result:
        result[age] = []
    
    result[age].append(name)

for age in sorted(result.keys()):
    for name in result[age]:
        sys.stdout.write(f"{age} {name}")
