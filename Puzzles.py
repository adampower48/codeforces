n, m = map(int, input().split())
puzzles = list(map(int, input().split()))

puzzles.sort()

minDiff = 1000000000

for i in range(0, m - n + 1):
    diff = puzzles[i + n - 1] - puzzles[i]
    # print("max: {}, min: {}".format(puzzles[i + n - 1], puzzles[i]))
    # print(diff)
    if diff < minDiff:
        minDiff = diff

print(minDiff)
