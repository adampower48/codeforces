def isWordValid():
    joinedBigWord = "".join(bigWord)

    return smallWord in joinedBigWord


bigWord = list(input())
print(bigWord)
smallWord = input()
order = list(map(int, input().split()))

turns = 0

for i in range(0, len(order)):
    bigWord[order[i] - 1] = ""
    if not isWordValid():
        break
    turns += 1

print(turns)
