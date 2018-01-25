n = int(input())
groups = list(map(int, input().split()))
taxiMax = 4

taxiCount = 0
curTaxi = 0

t4 = groups.count(4)
t3 = groups.count(3)
t2 = groups.count(2)
t1 = groups.count(1)

taxiCount += t4

# 3's
Groups31 = min(t3, t1)
taxiCount += Groups31
t3 -= Groups31
t1 -= Groups31
taxiCount += t3

# 2's
taxiCount += (t2 - t2 % 2) / 2
t2 -= (t2 - t2 % 2)

if t2 > 0:
    taxiCount += 1
    if t1 >= 2:
        t1 -= 2
    else:
        t1 = 0

# 1's
taxiCount += int(t1 / 4)
if t1 % 4 != 0:
    taxiCount += 1

print(int(taxiCount))
