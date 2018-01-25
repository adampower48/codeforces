n = int(input())
AScores = list(map(int, input().split()))
BScores = list(map(int, input().split()))
uniques = list()

for score in AScores:
    if score not in uniques:
        uniques.append(score)

for score in BScores:
    if score not in uniques:
        uniques.append(score)

switches = 0

for score in uniques:
    ACount = AScores.count(score)
    BCount = BScores.count(score)

    if (ACount + BCount) % 2 == 1:
        switches = -4
        break

    switches += abs(ACount - BCount)

print(int(switches / 4))
