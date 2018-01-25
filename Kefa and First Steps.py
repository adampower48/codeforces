n = int(input())
days = list(map(int, input().split()))

maxAsc = 0
curAsc = 0
last = 0

for d in days:
    if d >= last:
        curAsc += 1
    else:
        if curAsc > maxAsc:
            maxAsc = curAsc
        curAsc = 1
    last = d

if curAsc > maxAsc:
    maxAsc = curAsc

print(maxAsc)
