n = int(input())
coins = list(map(int, input().split()))

coins.sort()
coins.reverse()

halfway = sum(coins) / 2

totalCoins = 0
curTotal = 0

while curTotal <= halfway:
    curTotal += coins.pop(0)
    totalCoins += 1

print(totalCoins)
