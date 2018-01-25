n = int(input())

maxCap = 0
curCap = 0

for i in range(n):
    numExit, numEnter = map(int, input().split())
    curCap -= numExit
    curCap += numEnter
    maxCap = max(curCap, maxCap)

print(maxCap)
