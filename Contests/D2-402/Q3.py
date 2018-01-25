n, k = map(int, input().split())
week1 = list(map(int, input().split()))
week2 = list(map(int, input().split()))

difference = list()

for i in range(0, n):
    difference.append(week2[i] - week1[i])

money = 0

for i in range(0, k):
    index = difference.index(max(difference))
    money += week1.pop(index)
    week2.__delitem__(index)
    difference.__delitem__(index)

for i in range(0, len(difference)):
    if difference[i] > 0:
        money += week1[i]
    else:
        money += week2[i]

print(money)
