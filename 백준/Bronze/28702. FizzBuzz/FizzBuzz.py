import sys

num = 0
count = 0
result = ""

for i in range(3):
    fizz_buzz = sys.stdin.readline()
    try:
        num = int(fizz_buzz)
        count = i
    except ValueError:
        continue

num += 3 - count

if num % 3 == 0:
    result = "Fizz"

if num % 5 == 0:
    result = f"{result}Buzz"

if result == "":
    result = num

print(result)