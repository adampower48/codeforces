n = int(input())
rooms = 0

for i in range(0, n):
    p, q = map(int, input().split())
    if q - p >= 2:
        rooms += 1

print(rooms)
