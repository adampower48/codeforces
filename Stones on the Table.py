n = int(input())
stones = input()

numDoubles = 0

lastChar = "_"
for x in stones:
    # print("{} == {}: {}".format(lastChar, x, lastChar == x))
    if x == lastChar:
        numDoubles += 1
    lastChar = x

print(numDoubles)
