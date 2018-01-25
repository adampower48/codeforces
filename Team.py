n = int(input())

total = 0
for i in range(0, n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        total += 1

print(total)
