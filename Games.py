n = int(input())
homes = list()
aways = list()

for i in range(0, n):
    h, a = map(int, input().split())
    homes.append(h)
    aways.append(a)

games = 0

for colour in homes:
    games += aways.count(colour)

print(games)
