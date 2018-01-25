n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()
scores.reverse()

threshold = scores[k - 1]
winners = 0
for score in scores:
    if (score > 0) & (score >= threshold):
        winners += 1

print(winners)
