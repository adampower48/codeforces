n, k = map(int, input().split())

evenStart = 0

if n % 2 == 0:
    evenStart = n / 2 + 1
else:
    evenStart = (n + 3) / 2

if k < evenStart:
    print(int(k * 2 - 1))
else:
    print(int((k + 1 - evenStart) * 2))
