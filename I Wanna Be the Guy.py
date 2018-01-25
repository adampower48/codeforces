n = int(input())
aLevels = list(map(int, input().split()))[1::]
bLevels = list(map(int, input().split()))[1::]

for x in bLevels:
    if x not in aLevels:
        aLevels.append(x)

if len(aLevels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
