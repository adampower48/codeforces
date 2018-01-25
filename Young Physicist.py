n = int(input())

tX, tY, tZ = 0, 0, 0

for i in range(0, n):
    x, y, z = map(int, input().split())
    tX += x
    tY += y
    tZ += z

if tX == 0 & tY == 0 & tZ == 0:
    print("YES")
else:
    print("NO")
